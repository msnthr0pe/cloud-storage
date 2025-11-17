# app/services/auth_service.py
from uuid import uuid4
from datetime import datetime
from app.models.auth import RegisterRequest, RegisterResponse

class AuthService:
    def register(self, data: RegisterRequest) -> RegisterResponse:
        user_id = str(uuid4())
        return RegisterResponse(
            id=user_id,
            email=data.email,
            full_name=data.full_name,
            created_at=datetime.utcnow(),
        )
