# app/endpoints/auth_router.py
from fastapi import APIRouter
from app.models.auth import RegisterRequest, RegisterResponse
from app.services.auth_service import AuthService

auth_router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@auth_router.post("/register", response_model=RegisterResponse)
def register_user(request: RegisterRequest):
    service = AuthService()
    return service.register(request)
