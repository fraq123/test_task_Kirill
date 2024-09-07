from typing import List
from pydantic import BaseModel, RootModel


class ModelItem(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class GetPostsModel(RootModel[List[ModelItem]]):
    pass
