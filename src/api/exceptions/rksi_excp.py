from src.api.exceptions.global_exception import DolphineException


class RksiException(DolphineException):

    def __init__(self, name_st: str = "РКСИ") -> None:
        super().__init__(name_st)
