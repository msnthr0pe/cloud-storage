# app/services/access_service.py
from app.models.access_db import AccessDB

from app.db import SessionLocal
from app.models.access import AccessGrantRequest

class AccessService:
    async def grant_access(self, data: AccessGrantRequest):
        async with SessionLocal() as session:
            access = AccessDB(
                file_id=data.file_id,
                user_id=data.user_id,
                permission=data.permission
            )
            session.add(access)
            await session.commit()
