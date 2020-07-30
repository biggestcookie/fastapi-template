from aiohttp.client import ClientSession
from services.github import (
    async_fetch_authorized_github_user,
    fetch_authorized_github_user,
)
from fastapi import APIRouter
from pydantic import BaseModel
from requests import Session

router = APIRouter()


class HelloWorldResponse(BaseModel):
    payload: str


@router.get("", response_model=HelloWorldResponse)
def get(name: str = None) -> HelloWorldResponse:
    """Returns a 'Hello {name}!' response, or 'Hello world!' if name is not specified in the params."""
    payload = f"Hello { name or 'world' }!"
    body = {"payload": payload}
    return HelloWorldResponse(**body)


@router.get("/github")
def get_authorized_github_user():
    """Returns the GitHub user this application is authorized with."""
    with Session() as requests_session:
        return fetch_authorized_github_user(requests_session)


@router.get("/github/async")
async def async_get_authorized_github_user():
    """Returns the GitHub user this application is authorized with."""
    async with ClientSession() as aiohttp_session:
        return await async_fetch_authorized_github_user(aiohttp_session)
