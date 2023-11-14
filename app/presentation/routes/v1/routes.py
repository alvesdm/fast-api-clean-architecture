from fastapi import APIRouter

from .posts import router as posts_router

routers = APIRouter()
router_list = [posts_router]

for router in router_list:
    router.tags = routers.tags.append("v1/posts")
    routers.include_router(router)