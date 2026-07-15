from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.food.routes import router as food_router
from app.diary.routes import router as diary_router
from app.ocr.routes import router as ocr_router
from app.barcode.routes import router as barcode_router

app = FastAPI(title="Food Tracker API", version="0.1.0")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(food_router, prefix="/foods", tags=["foods"])
app.include_router(diary_router, prefix="/diary", tags=["diary"])
app.include_router(ocr_router, prefix="/ocr", tags=["ocr"])
app.include_router(barcode_router, prefix="/barcode", tags=["barcode"])


@app.get("/health")
def health():
    return {"status": "ok"}
