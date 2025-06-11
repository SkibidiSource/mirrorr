from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/mirror")
async def mirror_content(request: URLRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(request.url)
            response.raise_for_status()
        return {"content": response.text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
      
