from aiohttp.client import ClientSession
from fastapi import APIRouter
from requests import Session

from models.example import GitHubResponse, HelloWorldResponse
from services.github import (
    async_fetch_authorized_github_user,
    fetch_authorized_github_user,
    github_profile_to_example_response,
)

router = APIRouter()


@router.get("", response_model=HelloWorldResponse)
def hello_world(name: str = None) -> HelloWorldResponse:
    """Returns a 'Hello {name}!' response, or 'Hello world!' if name is not specified in the params."""
    payload = f"Hello { name or 'world' }!"
    body = {"payload": payload}
    return HelloWorldResponse(**body)


@router.get("/github", response_model=GitHubResponse)
def get_authorized_github_user() -> GitHubResponse:
    """Returns the GitHub user this application is authorized with."""
    with Session() as requests_session:
        resp_body = fetch_authorized_github_user(requests_session)
        return github_profile_to_example_response(resp_body)


@router.get("/github/async", response_model=GitHubResponse)
async def async_get_authorized_github_user() -> GitHubResponse:
    """Returns the GitHub user this application is authorized with."""
    async with ClientSession() as aiohttp_session:
        resp_body = await async_fetch_authorized_github_user(aiohttp_session)
        return github_profile_to_example_response(resp_body)
