from src.dolphine.parse_rgups.parser_rgups import RgupsParser
from src.api.dto.rgups_dto import (RGUPSGroupList, RGUPSLessonsList, RGUPSTypeEducationList)
from src.api.exceptions.rgups_excp import RgupsException
from typing import Type


class RgupsService:

    __rgups_parser: RgupsParser = RgupsParser()

    @classmethod
    async def get_groups(cls) -> RGUPSGroupList:
        data = cls.__rgups_parser.get_all_groups()
        if data:
            return RGUPSGroupList(groups=data)
        await RgupsException.excp_not_found_groups()

    @classmethod
    async def get_lessons(cls, name_group: str, type_faculity: str, course: str) -> RGUPSLessonsList:
        data = cls.__rgups_parser.get_lessons(
            name_facl=type_faculity,
            course_name=course,
            name_group=name_group
        )

        if data:
            return RGUPSLessonsList(lessons=data)
        await RgupsException.excp_not_found_name_st()

    @classmethod
    async def get_type_educations(cls) -> RGUPSTypeEducationList:
        data = cls.__rgups_parser.get_type_education_directions()
        if data:
            return RGUPSTypeEducationList(type_educations=data)
        await RgupsException.excp_not_found_type_educations()
