from src.dolphine.parser import Parser
from bs4 import BeautifulSoup
from typing import Union, Dict, List, Final
import re


class RksiParser(Parser):
    
    ELEMENTS_TO_REPLACE: Final[List[str]] = ["<p>", "p>", "<h3>", "h3>", "<b>", "b>", "r", "<b", "/>", "<h>"]

    def __init__(self) -> str:
        super().__init__(url="https://www.rksi.ru/schedule")
        self.bs_engine: Union[BeautifulSoup, None] = None

    @classmethod
    def replace_str_object(cls, str_object: str) -> str:
        for el in cls.ELEMENTS_TO_REPLACE:
            str_object = str_object.replace(el, "")
        return str_object
    
    def get_lessons(self, group: str) -> Dict[str, Union[dict, list, str]]: 
        
        html_data = self.get_html_data(group=group)
        
        if html_data:

            pattern = re.compile(f"<h3>{group}</h3>.*</p>")
            data = re.findall(pattern=pattern, string=html_data)
            data = data[0].split("</")

            lessons_data: Dict[Union[str, int], Union[str, int]] = dict()
            group_to_lessons_data: str = ""
            day: str = ""

            for str_obj in data:
                match str_obj:
                    case _ if "h3" in str_obj and "b" not in str_obj:
                        str_obj = self.replace_str_object(str_object=str_obj.strip())
                        group_to_lessons_data = str_obj.strip()
                        lessons_data[group_to_lessons_data.strip()] = {}
                    case _ if "b" in str_obj and any([el in str_obj for el in ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота")]):
                        str_obj = self.replace_str_object(str_object=str_obj)
                        if str_obj == "":
                            pass
                        else:
                            day = str_obj.strip()
                            lessons_data[group_to_lessons_data][day] = []
                    case _ if "p" in str_obj:
                        str_obj = self.replace_str_object(str_object=str_obj)
                        lessons_data[group_to_lessons_data][day].append(str_obj.strip())
                    case _ if "b" in str_obj:
                        str_obj = self.replace_str_object(str_object=str_obj)
                        lessons_data[group_to_lessons_data][day].append(str_obj.strip())
                    case _:
                        pass
            
            return lessons_data

    def get_teachers(self) -> List[str]:
        
        teachers_list: List[str] = str(self.get_selects_data()[-1])
        self.bs_engine = BeautifulSoup(teachers_list, "html.parser")
        return [option.get("value") for option in self.bs_engine.find_all("option")]
    
    def get_groups(self) -> List[str]:

        groups_list: List[str] = str(self.get_selects_data()[0])
        self.bs_engine = BeautifulSoup(groups_list, "html.parser")
        return [option.get("value") for option in self.bs_engine.find_all("option")]
        

    def get_html_data(self, group: str) -> Union[None, str]:
        
        req = self.session.post(url=self.url, data={"group": group, "stt": "Показать!"})
        if req.status_code == 200:
            return req.text
        return None
    
    def get_selects_data(self) -> list[str]:
        
        select_data: list[str] = self.session.get("https://www.rksi.ru/mobile_schedule").text
        self.bs_engine = BeautifulSoup(select_data, "html.parser")
        return self.bs_engine.find_all("select")