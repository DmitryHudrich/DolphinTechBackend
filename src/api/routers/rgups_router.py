from fastapi import APIRouter, status
from src.api.services.rgups_service import RgupsService, RGUPSGroupList, RGUPSLessonsList, RGUPSTypeEducationList
from typing import Type, Final


RGUPS_SERVICE: Final[Type[RgupsService]] = RgupsService()


rgups_router: Type[APIRouter] = APIRouter(
    prefix="/rgups",
    tags=["RGUPS"]
)

@rgups_router.get(
    path="/get_groups",
    description="""
    Получение всех учебных групп РГУПС
    """,
    summary="Список учебных групп",
    response_model=RGUPSGroupList,
    status_code=status.HTTP_200_OK
)
async def get_groups() -> RGUPSGroupList:
    return await RGUPS_SERVICE.get_groups()


@rgups_router.get(
    path="/get_lessons",
    description="""Получение расписания пар""",
    summary="Расписание пар РГУПС",
    response_model=RGUPSLessonsList,
    status_code=status.HTTP_200_OK
)
async def get_lessons(
    type_faculity: str,
    name_group: str,
    course: str
) -> RGUPSLessonsList:
    return await RGUPS_SERVICE.get_lessons(type_faculity=type_faculity, course=course, name_group=name_group)


@rgups_router.get(
    path="/get_type_educations",
    description="""Получение направлений""",
    summary="Учебные направления РГУПС",
    response_model=RGUPSTypeEducationList,
    status_code=status.HTTP_200_OK
)
async def get_type_educations() -> RGUPSTypeEducationList:
    return await RGUPS_SERVICE.get_type_educations()