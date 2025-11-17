from pydantic import EmailStr

from app.models.auth import RegisterRequest, RegisterResponse
from app.models.user_db import UserDB
from app.db import SessionLocal
from sqlalchemy.exc import IntegrityError
from datetime import datetime

class AuthService:
    async def register(self, data: RegisterRequest) -> RegisterResponse:
        async with SessionLocal() as session:
            db_user = UserDB(
                email=data.email,
                password=data.password,
                full_name=data.full_name,
            )
            session.add(db_user)
            try:
                await session.commit()
                await session.refresh(db_user)
            except IntegrityError:
                raise ValueError("Пользователь с таким email уже существует")
        return RegisterResponse(
            id=str(db_user.id),
            email=db_user.email,
            full_name=db_user.full_name,
            created_at=db_user.created_at,
        )
