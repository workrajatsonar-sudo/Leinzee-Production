import subprocess
import json
import re
import os
from typing import Dict, List, Optional

def extract_description(url: str) -> Dict:
    """
    Extract description from social media post using snscrape CLI.
    Supports Instagram, Facebook, and Twitter.
    """
    result = {
        "platform": None,
        "url": url,
        "description": None,
        "error": None
    }
    
    try:
        # Identify platform
        if "instagram.com" in url:
            result["platform"] = "instagram"
            post_id = extract_instagram_id(url)
            if not post_id:
                result["error"] = "Could not extract Instagram post ID"
                return result
            
            # Use snscrape CLI to get Instagram post
            # Instagram doesn't support direct post scraping via CLI, so we use hashtag/location workaround
            # For individual posts, we can try alternative method
            result["error"] = "Instagram individual posts require alternative method (see below)"
            
        elif "facebook.com" in url:
            result["platform"] = "facebook"
            post_id = extract_facebook_id(url)
            if not post_id:
                result["error"] = "Could not extract Facebook post ID"
                return result
            
            # Facebook scraping via snscrape CLI
            cmd = ["snscrape", "--jsonl", f"facebook-post", post_id]
            output = run_snscrape_command(cmd)
            
            if output:
                data = json.loads(output.split('\n')[0])
                result["description"] = data.get("content", "")
            
        elif "linkedin.com" in url:
            result["platform"] = "linkedin"
            # snscrape doesn't support LinkedIn, use alternative
            result["error"] = "LinkedIn not supported by snscrape. Use Selenium method below."
            
        else:
            result["error"] = f"Unsupported platform: {url}"
            
    except Exception as e:
        result["error"] = str(e)
    
    return result


def extract_instagram_id(url: str) -> Optional[str]:
    """Extract Instagram post/reel ID from URL"""
    patterns = [
        r'instagram\.com/p/([^/?&]+)',
        r'instagram\.com/reel/([^/?&]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def extract_facebook_id(url: str) -> Optional[str]:
    """Extract Facebook post ID from URL"""
    patterns = [
        r'facebook\.com/.*?/posts/(\d+)',
        r'fb\.com/.*?/posts/(\d+)',
        r'facebook\.com/groups/.*?/posts/(\d+)',
        r'facebook\.com/permalink\.php\?story_fbid=(\d+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def run_snscrape_command(cmd: List[str]) -> str:
    """Execute snscrape CLI command and return output"""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return ""
    except FileNotFoundError:
        raise Exception("snscrape not installed. Run: pip install snscrape")


# ============================================================================
# Alternative Method: Using yt-dlp (works for Instagram)
# ============================================================================

def extract_instagram_with_ytdlp(url: str) -> Dict:
    """
    Alternative method using yt-dlp to extract Instagram post info.
    Install: pip install yt-dlp
    """
    result = {
        "platform": "instagram",
        "url": url,
        "description": None,
        "error": None
    }
    
    try:
        import yt_dlp
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'force_generic_extractor': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            result["description"] = info.get("description", "")
            
    except ImportError:
        result["error"] = "yt-dlp not installed. Run: pip install yt-dlp"
    except Exception as e:
        result["error"] = str(e)
    
    return result


# ============================================================================
# Alternative Method: Using Selenium (works for LinkedIn)
# ============================================================================

def extract_linkedin_with_selenium(url: str) -> Dict:
    """
    Extract LinkedIn post description using Selenium.
    Install: pip install selenium webdriver-manager
    """
    result = {
        "platform": "linkedin",
        "url": url,
        "description": None,
        "error": None
    }
    
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        import time
        
        # Setup headless Chrome
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        try:
            driver.get(url)
            time.sleep(3)  # Wait for content to load
            
            # Try to find post content
            selectors = [
                "article .feed-shared-update-v2__description",
                ".feed-shared-text",
                "[data-test-id='main-feed-activity-card__commentary']",
                ".update-components-text"
            ]
            
            for selector in selectors:
                try:
                    element = driver.find_element(By.CSS_SELECTOR, selector)
                    result["description"] = element.text.strip()
                    break
                except:
                    continue
                    
        finally:
            driver.quit()
            
    except ImportError as e:
        result["error"] = f"Missing dependency: {e}. Install: pip install selenium webdriver-manager"
    except Exception as e:
        result["error"] = str(e)
    
    return result


# ============================================================================
# Main Unified Function
# ============================================================================

def extract_description_unified(url: str) -> Dict:
    """
    Extract description from any social media post using best available method.
    """
    if "instagram.com" in url:
        # Try yt-dlp first for Instagram
        return extract_instagram_with_ytdlp(url)
        
    elif "facebook.com" in url:
        # Use snscrape CLI for Facebook
        return extract_description(url)
        
    elif "linkedin.com" in url:
        # Use Selenium for LinkedIn
        return extract_linkedin_with_selenium(url)
        
    else:
        return {
            "platform": "unknown",
            "url": url,
            "description": None,
            "error": "Unsupported platform"
        }


# ============================================================================
# Test the code
# ============================================================================

if __name__ == "__main__":
    test_urls = [
        "https://www.instagram.com/p/DR4b8Zaj1Ye/",
        "https://www.facebook.com/Nintendo/posts/2257188721032235",
        "https://www.linkedin.com/feed/update/urn:li:activity:71234567890123456/"
    ]
    
    print("Extracting descriptions...\n")
    
    for url in test_urls:
        print(f"Processing: {url}")
        result = extract_description_unified(url)
        
        print(f"  Platform: {result['platform']}")
        if result.get('description'):
            desc = result['description'][:200]
            print(f"  Description: {desc}...")
        elif result.get('error'):
            print(f"  Error: {result['error']}")
        print("-" * 50)