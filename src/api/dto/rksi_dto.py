from pydantic import BaseModel, Field
from typing import List, Dict, Union, Annotated, Any


class RksiLessons(BaseModel):

    lessons: Annotated[Dict[Union[str, int], Union[str, int, List[Any], Dict[Any, Any]]], Field()]


class RksiGroups(BaseModel):

    groups: Annotated[Dict[str, List[str]], Field()]


class RksiTeachers(BaseModel):
    teachers: Annotated[Dict[str, List[str]], Field()]