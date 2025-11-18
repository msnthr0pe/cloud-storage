# app/endpoints/subscription_router.py
from fastapi import APIRouter, Depends, HTTPException
from app.models.subscription import SubscriptionResponse
from app.services.subscription_service import SubscriptionService
from app.dependencies import get_current_user

subscription_router = APIRouter()

@subscription_router.get("/api/subscription", response_model=SubscriptionResponse)
async def get_subscription(user_id: str = Depends(get_current_user)):
    service = SubscriptionService()
    try:
        return await service.get_subscription(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
