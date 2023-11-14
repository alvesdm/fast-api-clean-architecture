from __future__ import annotations # this is to allow a static method to return a type of itself

from pydantic import BaseModel
from app.domain.entities.post import Post

class PostModel(BaseModel):
    unique_id: str
    title: str
    content: str

    def to_entity(self) -> Post:
        return Post.from_dict(0, **self.__dict__)
    
    @staticmethod
    def from_entity(post: Post) -> PostModel:
        return PostModel(**post.__dict__)