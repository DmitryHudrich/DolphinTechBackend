from src.api.exceptions.global_exception import DolphineException


class IubipException(DolphineException):
    def __init__(self):
        super().__init__("ИУБИП")
