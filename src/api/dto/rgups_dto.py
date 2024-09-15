from pydantic import BaseModel, Field
from typing import List, Dict, Union, Annotated


class RGUPSGroupList(BaseModel):
    groups: Annotated[Dict[Union[str, int], Dict[Union[str, int], Union[List, int, str, Dict]]], Field()]

class RGUPSLessonsList(BaseModel):
    lessons: Annotated[Dict[Union[str, int], Dict[Union[str, int], Union[List, int, str, Dict]]], Field()]

class RGUPSTypeEducationList(BaseModel):
    type_educations: Annotated[Dict[str, Union[str, List[Union[str, int, Dict]], int, Union[int, str, Dict, List]]], Field()]
