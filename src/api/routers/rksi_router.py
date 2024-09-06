from fastapi import APIRouter, status
from typing import Type
from src.dolphine.parse_rksi.parser_rksi import RksiParser
from src.api.dto.rksi_dto import RksiGroups, RksiLessons, RksiTeachers
from src.api.services.rksi_service import RksiService


rksi_router: Type[APIRouter] = APIRouter(
    prefix="/rksi",
    tags=["RKSI"]
)


@rksi_router.get(
    path="/get_lessons/{name_group}",
    description="Получение расписания пар, занятий",
    response_model=RksiLessons,
    status_code=status.HTTP_200_OK
)
async def get_lessons(
    name_group: str
) -> RksiLessons:
    return await RksiService.get_lessons_for_student(name_group=name_group)


@rksi_router.get(
    path="/get_list_teachers",
    description="Получение списка актуальных преподавателей",
    response_model=RksiTeachers,
    status_code=status.HTTP_200_OK
)
async def get_teachers() -> RksiTeachers:
    return await RksiService.get_teachers_list()


@rksi_router.get(
    path="/get_list_schedule_groups",
    description="Получение списка учебных групп",
    response_model=RksiGroups,
    status_code=status.HTTP_200_OK
)
async def get_groups() -> RksiGroups:
    return await RksiService.get_schedule_groups()