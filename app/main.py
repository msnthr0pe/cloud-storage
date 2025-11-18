# app/main.py
from fastapi import FastAPI
from app.endpoints.auth_router import auth_router
from app.endpoints.profile_router import profile_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(profile_router)

