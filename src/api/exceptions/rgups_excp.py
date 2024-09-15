from fastapi.exceptions import HTTPException
from fastapi import status
from src.api.exceptions.global_exception import DolphineException


class RgupsException(DolphineException):
    def __init__(self):
        super().__init__(name_st="РГУПС")

    async def excp_not_found_type_educations(self):
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Не удалось найти учебные направления для {}" % self.name_st
        )