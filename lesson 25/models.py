from pydandtic import BaseModel


class MovieCreate(BaseModel):
    title: str
    director: str


class MovieUpdate(BaseModel):
    id:int