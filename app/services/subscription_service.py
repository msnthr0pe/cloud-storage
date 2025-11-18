# app/services/subscription_service.py
from app.db import SessionLocal
from app.models.subscription import SubscriptionResponse
from app.models.subscription_db import SubscriptionDB
from app.models.profile_db import ProfileDB

class SubscriptionService:
    async def get_subscription(self, user_id: str):
        async with SessionLocal() as session:
            subscription = await session.get(SubscriptionDB, user_id)
            if not subscription:
                raise ValueError("Подписка не найдена")
            profile = await session.execute(
                session.query(ProfileDB)
                .filter(ProfileDB.user_id == user_id)
            )
            profile = profile.scalar_one_or_none()
            if not profile:
                raise ValueError("Профиль не найден")
            return SubscriptionResponse(
                plan=subscription.plan,
                storage_limit=profile.storage_limit,
                storage_used=profile.storage_used,
                renewal_date=subscription.renewal_date,
            )
