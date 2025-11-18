# app/main.py
from fastapi import FastAPI

from app.endpoints.access_router import access_router
from app.endpoints.audit_log_router import audit_router
from app.endpoints.auth_router import auth_router
from app.endpoints.config_router import config_router
from app.endpoints.file_router import file_router
from app.endpoints.notification_router import notification_router
from app.endpoints.profile_router import profile_router
from app.endpoints.subscription_router import subscription_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(file_router)
app.include_router(access_router)
app.include_router(subscription_router)
app.include_router(notification_router)
app.include_router(audit_router)
app.include_router(config_router)

