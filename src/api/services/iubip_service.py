from src.api.exceptions.iubip_excp import IubipException
from src.dolphine.parse_iubip.parser_Iubip import IubipParser
from src.api.dto.iubip_dto import IubipLesson, IubipGroups


class IubipService:

    @staticmethod
    async def get_all_lessons_by_group(
        name_group: str
    ) -> IubipLesson:

        lessons = IubipParser().get_lessons(name_group=name_group)
        if lessons: return IubipLesson(lessons=lessons)
        await IubipException().excp_not_found_name_st()

    @staticmethod
    async def get_all_groups_and_falc() -> IubipGroups:

        groups = IubipParser().get_groups()
        if groups: return IubipGroups(lessons=groups)
        await IubipException().excp_not_found_groups()
