from src.dolphine_app import DolphineBackend
from fastapi import FastAPI
from typing import Type
from src.database.models.user_model import UserTable
from src.database.models.note_model import NoteTable
from src.database.worker import DBWorker


if __name__ == "__main__":
    dolphine_fst = DolphineBackend()
    app: Type[FastAPI] = dolphine_fst.back_app
    
    @app.on_event("startup")
    async def startup():
        await DBWorker.create_tables()

    dolphine_fst.start_project()