from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from v1 import routers

app = FastAPI()

app.include_router(routers.router)

@app.get("/")
async def index():
    return FileResponse("index.html")