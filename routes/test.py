from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class TestResponse(BaseModel):
    payload: str


@router.get("", response_model=TestResponse)
def test() -> TestResponse:
    res = {"payload": "Hello world!"}
    return TestResponse(**res)
