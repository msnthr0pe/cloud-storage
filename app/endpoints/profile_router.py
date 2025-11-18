from fastapi import APIRouter, HTTPException
from app.models.profile import ProfileResponse, ProfileUpdateRequest
from app.services.profile_service import ProfileService

profile_router = APIRouter(prefix="/api", tags=["Profile"])

@profile_router.get("/profile", response_model=ProfileResponse)
async def get_profile(user_id: str):
    service = ProfileService()
    try:
        return await service.get_profile(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail="Неверный формат user_id")

@profile_router.put("/profile")
async def update_profile(user_id: str, data: ProfileUpdateRequest):
    service = ProfileService()
    try:
        await service.update_profile(user_id, data)
        return {"message": "Profile updated successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
