from pydantic import BaseModel


class PostPalindromModel(BaseModel):
    id: str
    result: str

