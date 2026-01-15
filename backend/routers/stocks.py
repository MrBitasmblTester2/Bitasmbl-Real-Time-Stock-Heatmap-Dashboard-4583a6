from fastapi import APIRouter

router = APIRouter(prefix="/stocks")

@router.get("/sectors")
async def sectors():
    return []
