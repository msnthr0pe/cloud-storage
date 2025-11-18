from fastapi import APIRouter, HTTPException

from app.services.config_service import ConfigService

config_router = APIRouter(prefix="/api/config/get", tags=["Config"])

@config_router.get("")
async def get_config():
    service = ConfigService()
    try:
        return await service.get_config()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
