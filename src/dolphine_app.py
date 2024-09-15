import uvicorn
from fastapi import FastAPI, APIRouter
from src.admin.models.note_model_view import NoteAdmin
from src.admin.models.user_model_view import UserAdmin
from src.database.worker import DBWorker
from src.admin.admin_panel import AdminPanel


class DolphineBackend:
    def __init__(self) -> None:
        self.back_app: FastAPI = FastAPI(
            title="Дельфин бекенд", description="Делаем учебный процесс более удобным"
        )
        self.admin_panel: AdminPanel = AdminPanel(
            app=self.back_app, engine=DBWorker.engine
        )

        # Initialize model's view
        self.admin_panel.add_model_view(mdv=UserAdmin)
        self.admin_panel.add_model_view(mdv=NoteAdmin)

    def add_router(self, new_router: APIRouter) -> None:
        self.back_app.include_router(new_router)

    def start_project(self) -> None:
        uvicorn.run(app=self.back_app)
