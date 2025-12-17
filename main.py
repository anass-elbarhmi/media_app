from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import FileResponse

app = FastAPI()

# --- ENABLE CORS ---
# This allows your HTML file to communicate with this local API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   
@app.get("/")
def home():
    return FileResponse("HTML.html")
@app.get("/calculate_bmi")
def calculate_bmi(
    weight: float = Query(..., gt=20, lt=200, description="Weight in kg"), 
    height: float = Query(..., gt=1, lt=3, description="Height in meters")
):
    # Calculate BMI
    bmi = weight / (height * height)
    
    # Determine the message (English)
    message = ""
    if bmi < 18.5:
        message = "You are underweight. Consider a balanced diet to gain weight safely."
    elif 18.5 <= bmi < 25:
        message = "Your weight is ideal. Great job keeping healthy!"
    elif 25 <= bmi < 30:
        message = "You are overweight. Increasing physical activity is recommended."
    else:
        message = "You are in the obesity range. Please consult a doctor for advice."

    return {
        "bmi": bmi,
        "message": message
    }

if __name__ == "__main__":
    # Runs the server on port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)