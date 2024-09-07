from typing import Optional
from pydantic import BaseModel


class PutPosts1Model(BaseModel):
    id: int

