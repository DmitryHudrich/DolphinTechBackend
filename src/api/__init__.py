from fastapi import APIRouter
from typing import Type
from src.api.routers.rksi_router import rksi_router
from src.api.routers.iubip_router import iubip_router
from src.api.routers.rgups_router import rgups_router


api_v1: Type[APIRouter] = APIRouter(
    prefix="/api/v1",
    tags=["DolphineAPI"]
)

#Include
api_v1.include_router(rksi_router)
api_v1.include_router(iubip_router)
api_v1.include_router(rgups_router)