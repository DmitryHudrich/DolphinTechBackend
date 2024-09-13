from src.dolphine_app import DolphineBackend
from src.api import api_v1
from fastapi import FastAPI
from typing import Type
from src.database.worker import DBWorker
from src.dolphine.parse_iubip.parser_Iubip import IubipParser
from src.settings import Settings


if __name__ == "__main__":
    dolphine_fst = DolphineBackend()
    app: Type[FastAPI] = dolphine_fst.back_app
    
    @app.on_event("startup")
    async def startup():
        await DBWorker.create_tables()

    #api_v1
    dolphine_fst.add_router(api_v1)

    dolphine_fst.start_project()