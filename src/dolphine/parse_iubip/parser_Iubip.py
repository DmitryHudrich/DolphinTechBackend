from requests import Session
from bs4 import BeautifulSoup
from src.dolphine.parser import Parser
from src.settings import Settings
from typing import Union

class IubipParser(Parser):
    def __init__(self) -> None:
        super().__init__(url="https://www.iubip.ru/schedule")
        self.session: Session = Session()

    def get_lessons(self): pass

    def get_teachers(self): pass

    def get_groups(self) -> Union[None, dict]:
        req = self.session.post(
            url=Settings.iubip_group,
            data={"do": "groups"},
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0",
                "Origin": "https://www.iubip.ru"
            }
        )

        if req.status_code == 200:
            result_req: dict = req.json()
            return result_req
        return None