from fastapi import APIRouter
from typing import Type
from src.api.routers.rksi_router import rksi_router


api_v1: Type[APIRouter] = APIRouter(
    prefix="/api/v1",
    tags=["DolphineAPI"]
)

#Include
api_v1.include_router(rksi_router)