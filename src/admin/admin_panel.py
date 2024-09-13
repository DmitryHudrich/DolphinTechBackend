from fastapi import FastAPI
from sqladmin import Admin, ModelView
from typing import Type

from sqlalchemy.ext.asyncio import AsyncEngine


class AdminPanel:

    def __init__(self, app: Type[FastAPI], engine: Type[AsyncEngine]) -> None:
        self.admin_panel: Type[Admin] = Admin(
            app=app,
            engine=engine
        )

    def add_model_view(self, mdv: Type[ModelView]) -> None:
        self.admin_panel.add_view(mdv)