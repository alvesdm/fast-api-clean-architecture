from app.domain.entities.post import Post
from app.infrastructure.repository.posts_repository import IPostsRepository
from abc import ABC, abstractmethod

class IPostsService(ABC):
    @abstractmethod
    def get(self, id: str) -> Post:
        pass

    @abstractmethod
    def insert(self, post: Post):
        pass

class PostsService(IPostsService):
    def __init__(self, respository: IPostsRepository) -> None:
        self._respository = respository

    async def get(self, id: str) -> Post:
        return await self._respository.get(id)

    async def insert(self, post: Post):
        await self._respository.insert(post)