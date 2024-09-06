from fastapi import FastAPI, APIRouter
import uvicorn


class DolphineBackend:

    def __init__(self) -> None:
        self.back_app: FastAPI = FastAPI(
            title="Дельфин бекенд",
            description="Делаем учебный процесс более удобным"
        )

    def add_router(self, new_router: APIRouter) -> None:
        self.back_app.include_router(new_router) 

    def start_project(self) -> None:
        uvicorn.run(app=self.back_app)