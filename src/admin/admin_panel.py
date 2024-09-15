from fastapi import FastAPI
from sqladmin import Admin, ModelView

from sqlalchemy.ext.asyncio import AsyncEngine


class AdminPanel:
    def __init__(self, app: FastAPI, engine: AsyncEngine) -> None:
        self.admin_panel: Admin = Admin(app=app, engine=engine)

    def add_model_view(self, mdv: ModelView) -> None:
        self.admin_panel.add_view(mdv)
