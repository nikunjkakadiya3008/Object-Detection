from fastapi import APIRouter, Depends, File, UploadFile, WebSocket
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import json
import base64
from utils.objection_detect import detect_objects

router = APIRouter()

@router.get("/")
async def index_router():
    return FileResponse("index.html")


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            # Receive the frame as a base64-encoded string
            data = await websocket.receive_text()
            
            # Parse JSON data
            json_data = json.loads(data)
            image_data = json_data.get("image")
            if not image_data:
                continue
                
            # Convert base64 string to bytes
            _, base64_data = image_data.split(",", 1)
            image_bytes = base64.b64decode(base64_data)
            
            # Process the frame with YOLO
            detection_results = detect_objects(image_bytes)
            
            # Send detection results back to the client
            await websocket.send_json(detection_results)
            
    except Exception as e:
        print(f"WebSocket error: {e}")