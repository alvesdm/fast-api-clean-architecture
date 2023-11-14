from __future__ import annotations # this is to allow a static method to return a type of itself

class Post:
    id: str
    unique_id: str
    title: str
    content: str

    @staticmethod
    def from_dict(id:str, unique_id:str, title:str, content:str) -> Post:
        p = Post()
        p.id = id
        p.unique_id = unique_id
        p.title = title
        p.content = content

        return p