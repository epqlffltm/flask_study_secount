from fastapi import FastAPI
import uvicorn
import asyncio

app=FastAPI()

@app.get("/")
async def root():
    await asyncio.sleep(30)
    return {"hello": "world"}

if __name__ == "__main__":
    uvicorn.run("greet_async_uvicorn:app")