from abc import ABC, abstractmethod

from bson import ObjectId
from app.domain.entities.post import Post
from app.presentation.config import Config
from pymongo import MongoClient


class IPostsRepository(ABC):
    @abstractmethod
    def get(self, id: str) -> Post:
        pass

    def insert(self, post: Post) -> Post:
        pass

    def replace_id(self, entity):
        entity['id'] = str(entity['_id'])
        del(entity['_id'])
    
class PostsRepository(IPostsRepository):
    def __init__(self, configuration: Config) -> None:
        self._config = configuration
        self._client = MongoClient(configuration.POSTS_DB_CNN)
        self._posts_db = self._client["fastapi"]
        self._posts = self._posts_db["posts"]

    async def get(self, id: str) -> Post:
        post = self._posts.find_one(ObjectId(id))

        if post is None:
            return None
            
        self.replace_id(post)

        return Post.from_dict(**post)
    
    async def insert(self, post: Post) -> Post:
        p = post.__dict__
        del(p['id'])
        self._posts.insert_one(p)
        print("-->", p)
        self.replace_id(p)
        print("-->", post.id)
        return post
    
