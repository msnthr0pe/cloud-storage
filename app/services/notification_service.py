from sqlalchemy import select

from app.db import SessionLocal
from app.models.notification import NotificationItem
from app.models.notification_db import NotificationDB


class NotificationService:
    async def get_notifications(self, user_id: str, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        async with SessionLocal() as session:
            stmt = (
                select(NotificationDB)
                .where(NotificationDB.user_id == user_id)
                .order_by(NotificationDB.created_at.desc())
                .offset(offset)
                .limit(limit)
            )
            result = await session.execute(stmt)
            notifications = result.scalars().all()
            return [NotificationItem(**n.__dict__) for n in notifications]
