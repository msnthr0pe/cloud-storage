# app/models/auth.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class RegisterResponse(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    created_at: datetime
