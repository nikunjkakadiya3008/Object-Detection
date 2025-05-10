# Object-Detection
Implementing Real-Time Object Detection on Live Video Streams Using YOLOv8 (Meta's Ultralytics Framework)

## Frameworks Used
- **FastAPI** – For building the REST API backend
- **Uvicorn** – ASGI server for running FastAPI
- **YOLOv8 (Ultralytics)** – For object detection
- **Python 3.8+**

## Project Setup and Usage

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd Object-Detection
```

### 2. Set Up the Environment
- Copy the example environment file and update it as needed:
  ```sh
  cp env.example .env
  ```
- (Optional) Create and activate a virtual environment:
  ```sh
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Download/Verify YOLOv8 Model
- Ensure the YOLOv8 model file (`model/yolov8l.pt`) is present in the `model/` directory.

### 5. Run the Application
```sh
uvicorn main:main --reload
```
- This will start the server with auto-reload and initialize the object detection pipeline.

### 6. Access the Application
- Open [index.html](index.html) in your browser or use the provided API endpoints (see below).

### 7. API Endpoints
- The API endpoints are defined in [`v1/routers.py`](v1/routers.py) and [`v1/server.py`](v1/server.py).
- Example endpoints:
  - `/detect` – For object detection on uploaded images or video streams.

### 8. Project Structure
- `main.py`: Entry point for the application.
- `v1/`: Contains core modules (routers, database, schemas, etc.).
- `utils/objection_detect.py`: Contains object detection logic using YOLOv8.
- `model/`: Stores the YOLOv8 model file.
- `index.html`: Frontend interface (if applicable).

### 9. Customization
- Modify detection logic in [`utils/objection_detect.py`](utils/objection_detect.py).
- Update API routes in [`v1/routers.py`](v1/routers.py).

### 10. Testing
- Add or run tests as needed to ensure functionality.

---

**For more details, see comments and docstrings in each module.**
