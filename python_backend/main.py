from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import instaloader
import re
from datetime import datetime, timedelta

app = FastAPI()


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Backend is running",
        "docs": "/docs",
        "extract": "/extract?url=https://www.instagram.com/reel/SHORTCODE/"
    }


@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)


# Allow CORS so the Vite React app can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

L = instaloader.Instaloader()

def extract_shortcode(url: str) -> str:
    """Extracts the shortcode from an Instagram reel or post URL."""
    # Handle various formats: /reel/ABC123XYZ/, /reels/ABC123XYZ/, /p/ABC123XYZ/
    match = re.search(r'/(?:reel|reels|p)/([a-zA-Z0-9_-]{3,})', url)
    if match:
        return match.group(1)
    return None

@app.get("/extract")
def extract_reel(url: str):
    print(f"Extracting URL: {url}")
    shortcode = extract_shortcode(url)
    if not shortcode:
        raise HTTPException(status_code=400, detail="Invalid Instagram URL. Expected /reel/SHORTCODE/ or /reels/SHORTCODE/")
    
    try:
        # Load post using instaloader
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        caption = post.caption or ""
        
        # Parse the first meaningful sentence as the Task Title
        lines = [line.strip() for line in caption.split("\n") if line.strip() and not line.strip().startswith("#")]
        
        # If no non-hashtag lines found, use the first hashtag or a default
        if not lines:
            hashtags = [part for part in caption.split() if part.startswith("#")]
            title = hashtags[0] if hashtags else "Actionable Task"
        else:
            title = lines[0]
            
        # Truncate title if it's too long
        if len(title) > 80:
            title = title[:77] + "..."
            
        # Extract hashtags separately for metadata
        tags = re.findall(r'#(\w+)', caption)
        
        # Give a 7 day deadline default
        deadline = (datetime.now() + timedelta(days=7)).isoformat()
        
        return {
    "title": title,
    "description": caption,
    "shortcode": shortcode,
    "deadline": deadline,
    "hashtags": tags[:5],
    "thumbnail": post.url  # This gets the main image/video thumbnail from Instaloader
}
    except Exception as e:
        print(f"Instaloader error: {str(e)}")
        # If login is required or blocked, we might get a 401 or similar
        raise HTTPException(status_code=500, detail=f"Failed to fetch reel: {str(e)}")
