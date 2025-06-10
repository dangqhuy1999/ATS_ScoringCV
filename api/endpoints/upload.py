# ✅ File: api/endpoints/upload.py
from fastapi import APIRouter, UploadFile, File
from api.schemas import UploadResponse
from api.services.file_handler import FileHandler

router = APIRouter()

@router.post("/", response_model=UploadResponse)
async def upload_cv(file: UploadFile = File(...)):
    handler = FileHandler()
    filename = handler.save_file(file)
    return UploadResponse(filename=filename, status="uploaded")

