from fastapi import APIRouter, HTTPException

from app.models.auth import LoginRequest, LoginResponse
from app.models.auth import RegisterRequest, RegisterResponse
from app.services.auth_service import AuthService

auth_router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@auth_router.post("/register", response_model=RegisterResponse)
async def register_user(request: RegisterRequest):
    service = AuthService()
    try:
        return await service.register(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))

@auth_router.post("/login", response_model=LoginResponse)
async def login_user(request: LoginRequest):
    service = AuthService()
    try:
        return await service.login(request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))