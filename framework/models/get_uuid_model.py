from pydantic import BaseModel, RootModel


class GetUuidModel(BaseModel):
    result: str
