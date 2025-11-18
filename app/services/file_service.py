# app/services/file_service.py
from sqlalchemy import select

from app.db import SessionLocal
from app.models.file import FileUploadResponse, FileDownloadResponse
from app.models.file_db import FileDB
from app.dependencies import get_current_user


class FileService:
    async def upload_file(self, file, user_id, parent_id=None):
        filename = file.filename
        contents = await file.read()
        size = len(contents)
        # Можно сохранить физически: сэтимпу пути, если требуется
        # with open(os.path.join("uploads", filename), "wb") as f:
        #     f.write(contents)
        new_file = FileDB(
            name=filename,
            size=size,
            user_id=user_id,
            parent_id=parent_id,
        )
        async with SessionLocal() as session:
            session.add(new_file)
            await session.commit()
            await session.refresh(new_file)
        return FileUploadResponse(
            id=new_file.id,
            name=new_file.name,
            size=new_file.size,
            uploaded_at=new_file.uploaded_at,
        )

    async def get_file_name(self, file_id: str):
        async with SessionLocal() as session:
            result = await session.execute(
                select(FileDB).where(FileDB.id == file_id)
            )
            file = result.scalar_one_or_none()
            if file is None:
                raise ValueError("Файл не найден")
            return FileDownloadResponse(name=file.name)

    async def delete_file(self, file_id: str):
        async with SessionLocal() as session:
            result = await session.execute(
                select(FileDB).where(FileDB.id == file_id)
            )
            file = result.scalar_one_or_none()
            if file is None:
                raise ValueError("Файл не найден")
            await session.delete(file)
            await session.commit()
