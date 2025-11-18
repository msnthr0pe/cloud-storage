from fastapi import APIRouter, Depends, HTTPException
from app.models.access import AccessGrantRequest
from app.services.access_service import AccessService
from app.dependencies import get_current_user

access_router = APIRouter(prefix="/api/access", tags=["Access"])

@access_router.post("/grant")
async def grant_access(data: AccessGrantRequest, _: str = Depends(get_current_user)):
    service = AccessService()
    try:
        await service.grant_access(data)
        return {"message": "Access granted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
