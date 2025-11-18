from fastapi import APIRouter, Depends, Query
from app.models.notification import NotificationItem
from app.services.notification_service import NotificationService
from app.dependencies import get_current_user

notification_router = APIRouter(tags=["Notifications"])

@notification_router.get("/api/notifications", response_model=list[NotificationItem])
async def get_notifications(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    user_id: str = Depends(get_current_user)
):
    service = NotificationService()
    return await service.get_notifications(user_id, page, limit)
