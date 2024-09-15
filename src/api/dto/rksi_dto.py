from pydantic import BaseModel, Field
from typing import List, Dict, Union, Annotated, Any


class RksiLessons(BaseModel):
    lessons: Annotated[
        Dict[Union[str, int], Union[str, int, List[Any], Dict[Any, Any]]], Field()
    ]


class RksiGroups(BaseModel):
    groups: Annotated[List[str], Field()]


class RksiTeachers(BaseModel):
    teachers: Annotated[List[str], Field()]
