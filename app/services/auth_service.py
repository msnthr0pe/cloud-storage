import time

from sqlalchemy import select

from app.models.auth import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse
from app.models.user_db import UserDB
from app.db import SessionLocal
from sqlalchemy.exc import IntegrityError
from app.models.profile_db import ProfileDB
from app.dependencies import get_current_user
import jwt

SECRET_KEY = "supersecret"      # для учебного кейса

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

            # После успешного коммита добавляем профиль
            db_profile = ProfileDB(
                user_id=db_user.id,  # связь с users.id
                storage_used=0,
                storage_limit=2147483647  # лимит по ТЗ
            )
            session.add(db_profile)
            await session.commit()
            await session.refresh(db_profile)

        return RegisterResponse(
            id=str(db_user.id),
            email=db_user.email,
            full_name=db_user.full_name,
            created_at=db_user.created_at,
        )

    async def login(self, data: LoginRequest) -> LoginResponse:
        async with SessionLocal() as session:
            result = await session.execute(
                select(UserDB).where(
                    UserDB.email == data.email,
                    UserDB.password == data.password
                )
            )
            user = result.scalar_one_or_none()
            if user is None:
                raise ValueError("Неверный email или пароль")
            payload = {
                "sub": str(user.id),
                "email": user.email,
                "exp": int(time.time()) + 3600*24,
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return LoginResponse(access_token=token, expires_in=3600*24)
