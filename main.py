import uvicorn
from v1.server import app

main = app  # Add this line to expose 'main' as the ASGI app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080, log_level="info")
