from src.dolphine.parse_rksi.parser_rksi import RksiParser
from src.api.dto.rksi_dto import RksiGroups, RksiLessons, RksiTeachers
from src.api.exceptions.rksi_excp import RksiException
from typing import List


class RksiService:

    rksi_parser = RksiParser()

    @classmethod
    async def get_lessons_for_student(cls, name_group: str) -> RksiLessons:
        lessons: list = cls.rksi_parser.get_lessons(group=name_group)
        if lessons:
            return RksiLessons(lessons=lessons)
        await RksiException.excp_not_found_name_st()

    @classmethod
    async def get_teachers_list(cls) -> RksiTeachers:
        teachers_lst: List[str] = cls.rksi_parser.get_teachers()
        teachers_lst = [teacher for teacher in teachers_lst if "_" not in teacher]
        if teachers_lst:
            return RksiTeachers(teachers=teachers_lst)
        await RksiException.excp_not_found_teachers()

    @classmethod
    async def get_schedule_groups(cls) -> RksiGroups:
        groups_list: List[str] = cls.rksi_parser.get_groups()
        if groups_list:
            return RksiGroups(groups=groups_list)
        raise RksiException.excp_not_found_groups()
