from pydantic import BaseModel, Field
from typing import Dict, List, Any, Union, Annotated


class IubipLesson(BaseModel):
    lessons: Annotated[Dict[Union[List, Dict, int, str], Union[List, Dict, int, str]], Field()]

class IubipGroups(BaseModel):
    lessons: Annotated[Dict[Union[List, Dict, int, str], Union[List, Dict, int, str]], Field()]