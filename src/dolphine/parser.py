from abc import ABC, abstractclassmethod
from requests import Session


class Parser:
    def __init__(self, url: str) -> str:
        self.url = url
        self.session: Session = Session()

    @abstractclassmethod
    def get_lessons(*args, **kwargs):
        pass

    @abstractclassmethod
    def get_teachers(*args, **kwargs):
        pass
