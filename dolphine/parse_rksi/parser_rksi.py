from dolphine.parser import Parser
from bs4 import BeautifulSoup
from typing import Union, Dict, List, Final
import re


class RksiParser(Parser):
    
    ELEMENTS_TO_REPLACE: Final[List[str]] = ["<p>", "p>", "<h3>", "h3>", "<b>", "b>", "r", "<b", "/>"]

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
                        str_obj = self.replace_str_object(str_object=str_obj)
                        group_to_lessons_data = str_obj
                        lessons_data[group_to_lessons_data.strip()] = {}
                    case _ if "b" in str_obj and "p" not in str_obj and "br" not in str_obj:
                        str_obj = self.replace_str_object(str_object=str_obj)
                        lessons_data[group_to_lessons_data][str_obj.strip()] = []
                        day = str_obj
                    case _ if "p" in str_obj:
                        str_obj = self.replace_str_object(str_object=str_obj)
                        lessons_data[group_to_lessons_data][day].append(str_obj.strip())
                    case _ if "b" in str_obj:
                        str_obj = self.replace_str_object(str_object=str_obj)
                        lessons_data[group_to_lessons_data][day].append(str_obj.strip())
                    case _:
                        pass
            
            return lessons_data

    def get_teachers(self, *args, **kwargs) -> None: pass

    def get_html_data(self, group: str) -> Union[None, str]:
        
        req = self.session.post(url=self.url, data={"group": group, "stt": "Показать!"})
        if req.status_code == 200:
            return req.text
        return None