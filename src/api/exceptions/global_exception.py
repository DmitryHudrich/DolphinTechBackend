from fastapi import HTTPException, status


class DolphineException(HTTPException):

    def __init__(self, name_st: str = "Учебное заведение") -> None:
         self.name_st: str = name_st

    async def excp_not_found_name_st(self):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Не удалось найти нужную информацию в {}".format(self.name_st),
        )
    
    async def excp_not_found_teachers(self):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Не удалось найти список преподавателей в {}".format(self.name_st)
        )