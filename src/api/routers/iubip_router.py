from fastapi import APIRouter, status
from src.api.dto.iubip_dto import IubipLesson
from src.api.services.iubip_service import IubipService, IubipGroups


iubip_router: APIRouter = APIRouter(
    prefix="/iubip",
    tags=["IUBIP Schedule"]
)


@iubip_router.get(
    path="/get_lessons",
    description="Получение полного расписания занятий",
    response_model=IubipLesson,
    status_code=status.HTTP_200_OK
)
async def get_lessons(
    name_group: str
) -> IubipLesson:
    return await IubipService.get_all_lessons_by_group(name_group=name_group)


@iubip_router.get(
    path="/get_groups",
    description="Получение списка имеющихся учебных групп",
    response_model=IubipGroups,
    status_code=status.HTTP_200_OK
)
async def get_groups() -> IubipGroups:
    return await IubipService.get_all_groups_and_falc()