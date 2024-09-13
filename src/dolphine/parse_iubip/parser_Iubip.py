import json
from operator import index
from textwrap import indent

from requests import Session
from bs4 import BeautifulSoup
from src.dolphine.parser import Parser
from src.settings import Settings
from typing import Union

class IubipParser(Parser):
    def __init__(self) -> None:
        super().__init__(url="https://www.iubip.ru/schedule")
        self.session: Session = Session()

    def get_lessons(self, name_group: str) -> Union[None, dict]:
        req = self.session.post(
            url=Settings.iubip_group,
            data={
                "do": "schedule",
                "group": name_group
            }
        )

        if req.status_code == 200:
            result = req.json()
            if result:
                lessons_for_group: dict = {}
                lessons_for_group["Период расписания"] = result.get(name_group)[0]
                periods_cnt: int = 0

                for data in result.get(name_group)[1]:
                    for data_period in result.get(name_group)[1].get(data):
                        if "per" in data_period:
                            lessons_for_group[data_period.get("per").strip()] = {}
                            period = data_period.get("per")
                        else:
                            for lesson in data_period.values():
                                lesson_date = list(lesson.values())[0]
                                for lesson_day in lesson:
                                    lesson_day = lesson[lesson_day][0]
                                    day = lesson_day.get("DATE").strip()
                                    if day not in lessons_for_group[period]:
                                        lessons_for_group[period][day] = []
                                    lessons_for_group[period][day].append(
                                        {
                                            "GROUP": lesson_day.get("GROUP").strip() if lesson_day.get("GROUP") else None,
                                            "LES": lesson_day.get("LES").strip() if lesson_day.get("DAY") else None,
                                            "AUD": lesson_day.get("AUD").strip() if lesson_day.get("LES") else None,
                                            "NAME_TEACHER": lesson_day.get("NAME").strip() if lesson_day.get(
                                                "NAME") else None,
                                            "LESSON": lesson_day.get("SUBJECT").strip() if lesson_day.get(
                                                "SUBJECT") else None,
                                            "CAFEDRA": lesson_day.get("CAFEDRA").strip() if lesson_day.get(
                                                "CAFEDRA") else None,
                                            "FACULITY": lesson_day.get("FACULITY").strip() if lesson_day.get(
                                                "FACULITY") else None,
                                            "DATE": lesson_day.get("DATE")
                                        }
                                    )
                return lessons_for_group
        return None

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