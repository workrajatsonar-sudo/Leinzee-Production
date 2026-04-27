from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import StreamingResponse
import requests
from io import BytesIO

app = FastAPI()

@app.get('/proxy-image')
def proxy_image(url: str = Query(..., description="Image URL to proxy")):
    try:
        r = requests.get(url, stream=True, timeout=10)
        r.raise_for_status()
        content_type = r.headers.get('Content-Type', 'image/jpeg')
        return StreamingResponse(BytesIO(r.content), media_type=content_type)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch image: {e}")
