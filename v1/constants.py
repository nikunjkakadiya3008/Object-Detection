from dotenv import load_dotenv
import os
load_dotenv()

# Constants for the application
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# HTTP Status Codes
HC_OK = 200
HC_CREATED = 201
HC_BAD_REQUEST = 400
HC_ISE = 500

