from fastapi import APIRouter

router = APIRouter(
    prefix="/posts",
    #tags=["post"],
)

@router.get("")
async def get_post_list():
    return "my posts v2"