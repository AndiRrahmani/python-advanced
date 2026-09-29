from pydantic import BaseModel
from typing import List,Optional

class Developer(BaseModel):
    name: str
    experience: Optional[int]=None

class Project(BaseModel):
    title: str
    dscription: Optional[str]=None
    language: Optional[list[str]]=None
    lead_developer: Developer