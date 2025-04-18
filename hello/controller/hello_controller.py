from fastapi import APIRouter
from fastapi.responses import JSONResponse

helloRouter = APIRouter()

@helloRouter.get("/")
async def requestHome():
    return JSONResponse(
        content={"message": "Hello Deploy Test"},
        status_code=200
    )
