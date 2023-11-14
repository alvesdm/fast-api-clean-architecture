from fastapi.responses import PlainTextResponse
from app.presentation.container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from app.application.services.posts_service import IPostsService
from app.presentation.exception_handling import CustomNotFoundError
from app.presentation.models.post_model import PostModel

router = APIRouter(
    prefix="/posts",
    #tags=["post"],
)

@router.get("/id")
@inject
async def get_post(id: str, post_service: IPostsService = Depends(Provide[Container.post_service])):
    post = await post_service.get(id)

    if post is None:
        raise CustomNotFoundError("It seems like the post you were looking for does not exist.")
    
    return PostModel.from_entity(post)

@router.post("", status_code=status.HTTP_201_CREATED)
@inject
async def insert_post(model: PostModel, post_service: IPostsService = Depends(Provide[Container.post_service])):
    post = model.to_entity()
    await post_service.insert(post)

    return PlainTextResponse("OK", status.HTTP_201_CREATED, {"Location" : f"/api/v1/posts/{post.id}"} )