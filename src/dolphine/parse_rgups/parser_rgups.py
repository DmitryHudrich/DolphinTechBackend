from src.dolphine.parser import Parser
from src.settings import Settings
from typing import List, Dict, Union, Type
from requests import Session
from bs4 import BeautifulSoup, Tag


class RgupsParser(Parser):
    def __init__(self) -> None:
        super().__init__(url=Settings.rgups_url)
        self.session: Type[Session] = Session()

    def get_html_data(self) -> str:
        req = self.session.get(self.url)
        if req.status_code == 200:
            return req.content

    def get_type_education_directions(self) -> Union[None, Dict[str, Union[str, List[Union[str, int]], int]]]:
        html_data = self.get_html_data()
        if html_data:
            bs = BeautifulSoup(html_data, "lxml")
            schedule_faculity = bs.find_all("div", class_="schedule-section faculty")
            groups_data: Dict = {"ochnoe": [], "zaochnoe": []}
            cnt_type_faculty: Dict[int, str] = {0: "ochnoe", 1: "zaochnoe"}
            cnt_faculty: int = 0

            for faculty in schedule_faculity:

                for facl in faculty:
                    if type(facl) is Tag:
                        tag_faculty = facl.get("data-fac-id")
                    facl = str(facl)
                    if facl.isalpha() or facl == "Аспирантура и докторантура":
                        groups_data[cnt_type_faculty[cnt_faculty]].append({
                            "name_group": facl,
                            "group-facl-id": tag_faculty
                        })
                cnt_faculty += 1

            return groups_data
        return None

    def get_groups_for_faculty(self, type_education: str, name_faculty: str) -> Union[None, Dict[str, Union[str, List[Union[int, str]], int]]]:

        if type_education == "Очное":
            edu_type = "internal"
        elif type_education == "Заочное":
            edu_type = "distance"

        group_facl_id: str = self.get_type_education_directions()
        group_id: Union[int, None] = None
        if group_facl_id:
            group_facl_id = group_facl_id["ochnoe" if type_education == "Очное" else "zaochnoe"]
            for group in group_facl_id:
                if group.get("name_group") == name_faculty:
                    group_id = group.get("group-facl-id")
                    break
        if group_id:
            req = self.session.post(
                url=self.url,
                data={
                    "action": "course",
                    "fac-id": group_id,
                    "edu_type": edu_type
                }
            )

            if req.status_code == 200:
                html_data_courses = BeautifulSoup(req.content, "lxml")
                courses_data: dict = {}

                for cs_d in html_data_courses.find_all("a"):
                    courses_data[cs_d.text] = {"course_id": cs_d.get("data-course-id")}
                return courses_data

    def get_group_id(self, type_education: str, name_facl: str, course: str, name_group: str) -> str:
        req = self.session.post(
            url = self.url,
            data = {
                "action": "groups",
                "fac-id": [name.get("group-facl-id") for name in self.get_type_education_directions()["ochnoe" if type_education == "Очное" else "zaochnoe"]
                           if name.get("name_group") == name_facl][0],
                "course-id": course[0],
                "edu-type": "internal" if type_education == "Очное" else "distance"
            }
        )

        if req.status_code == 200:
            html_data: str = BeautifulSoup(req.content, "lxml")
            for data_group in html_data.find_all("a"):
                if data_group.text == name_group:
                    return data_group.get("data-group-id")
        return None

    ##TOO SLOW
    def get_all_groups(self) -> Dict[str, Dict[str, List[str]]]:

        type_facl: tuple = ("ochnoe", "zaochnoe")
        facl_data = self.get_type_education_directions()
        all_groups: Dict[str, Dict[str, List[str]]] = {
            "internal": {
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": []
            },
            "distance": {
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": []
            }
        }

        if facl_data:
            for t_f in type_facl:
                for fcl in facl_data[t_f]:
                    for course in range(1, 6):
                        html_data_groups = self.session.post(
                            url=self.url,
                            data={
                                "action": "groups",
                                "fac-id": fcl.get("group-facl-id"),
                                "course-id": str(course),
                                "edu-type": "internal"
                            }
                        )

                        if html_data_groups.status_code == 200:
                            soap = BeautifulSoup(html_data_groups.content, "lxml")
                            all_groups["internal" if t_f == "ochnoe" else "distance"][str(course)].extend([
                                    gr_d.text for gr_d in soap.find_all("a")
                                ]
                            )
            return all_groups

    def get_lessons(self, name_facl: str, course_name: str, name_group: str) -> Dict:
        pass

    def get_teachers(self, *args): pass