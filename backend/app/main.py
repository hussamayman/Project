from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .schemas import PredictResponse
from .services.predictor import predict_dummy

app = FastAPI(title="Tank Guide API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
async def predict(image: UploadFile = File(...)):
    # image ignored for now (dummy mode)
    result = predict_dummy()
    return result
