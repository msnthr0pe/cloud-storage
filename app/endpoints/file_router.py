# app/endpoints/file_router.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.file_service import FileService
from app.models.file import FileUploadResponse

file_router = APIRouter(prefix="/api/files", tags=["Files"])

@file_router.post("/upload", response_model=FileUploadResponse)
async def upload_file(
    file: UploadFile = File(...),
    user_id: str = Form(...),
    parent_id: str = Form(None)
):
    service = FileService()
    try:
        return await service.upload_file(file, user_id, parent_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
