# app/services/profile_service.py
from sqlalchemy.future import select

from app.db import SessionLocal
from app.models.profile_db import ProfileDB
from app.models.user_db import UserDB
from app.models.profile import ProfileResponse

class ProfileService:
    async def get_profile(self, user_id: str) -> ProfileResponse:
        async with SessionLocal() as session:
            user_result = await session.execute(select(UserDB).where(UserDB.id == user_id))
            user = user_result.scalar_one_or_none()
            profile_result = await session.execute(select(ProfileDB).where(ProfileDB.user_id == user_id))
            profile = profile_result.scalar_one_or_none()
            if not user or not profile:
                raise ValueError("Профиль или пользователь не найден")
            return ProfileResponse(
                id=str(user.id),
                email=user.email,
                full_name=user.full_name,
                storage_used=profile.storage_used,
                storage_limit=profile.storage_limit,
                created_at=user.created_at,
            )
