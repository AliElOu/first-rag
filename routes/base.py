from fastapi import APIRouter
import os
base_router = APIRouter()


@base_router.get("/")
def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "message": f"Welcome to {app_name} v{app_version}!"
    }