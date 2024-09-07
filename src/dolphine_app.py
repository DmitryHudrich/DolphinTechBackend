import uvicorn
from fastapi import FastAPI, APIRouter
from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from src.admin_models.models_for_admin_panel import UserAdmin, NoteAdmin
from src.database.worker import DBWorker


class DolphineBackend:

    def __init__(self) -> None:
        self.back_app: FastAPI = FastAPI(
            title="Дельфин бекенд",
            description="Делаем учебный процесс более удобным"
        )
        self.admin_panel: Admin = Admin(app=self.back_app, engine=DBWorker.engine)
        self.admin_panel.add_view(UserAdmin)
        self.admin_panel.add_view(NoteAdmin)

    def add_router(self, new_router: APIRouter) -> None:
        self.back_app.include_router(new_router) 

    def start_project(self) -> None:
        uvicorn.run(app=self.back_app)