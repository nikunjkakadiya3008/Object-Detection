from ultralytics import YOLO
from PIL import Image
import io
import base64
import os
from urllib.request import urlretrieve

model_dir = 'model'
model_path = os.path.join(model_dir, 'yolov8l.pt')

# Create the directory if it doesn't exist
os.makedirs(model_dir, exist_ok=True)

model = YOLO(model_path)

def detect_objects(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    results = model(image, verbose=False)
    detections = []
    
    original_width, original_height = image.size
    
    for r in results:
        for i, box in enumerate(r.boxes):
            box_coords = [float(x) for x in box.xyxy[0]]
            class_id = int(box.cls)
            class_name = model.names[class_id]
            confidence = float(box.conf)
            
            # Only keep detections with confidence > 0.5
            if confidence <= 0.5:
                continue
            
            # Ensure box coordinates are within image bounds
            x1, y1, x2, y2 = max(0, int(box_coords[0])), max(0, int(box_coords[1])), \
                             min(original_width, int(box_coords[2])), min(original_height, int(box_coords[3]))
            
            # Crop the detected object
            if x2 > x1 and y2 > y1:  # Ensure valid crop area
                cropped_img = image.crop((x1, y1, x2, y2))
                
                # Convert cropped image to base64 encoded string
                buffered = io.BytesIO()
                cropped_img.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
                
                # Add cropped image data to the detection
                detection = {
                    "class": class_name,
                    "confidence": confidence,
                    "box": box_coords,
                    "id": f"{class_name}_{i}",
                    "cropped_image": img_str
                }
                detections.append(detection)

    return {"detections": detections}


