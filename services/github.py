import os
from typing import Any

from aiohttp import ClientSession
from dotenv import load_dotenv
from requests import Session


load_dotenv()
TOKEN = os.getenv("github_token")
HEADERS = {"Authorization": f"token {TOKEN}"}
API_BASE_URL = "https://api.github.com"
API_USER_URL = f"{API_BASE_URL}/user"


def fetch_authorized_github_user(requests_session: Session):
    """Synchronously fetches and returns the current authorized GitHub user.
    Uses the requests module.
    """
    with requests_session.get(API_USER_URL, headers=HEADERS) as response:
        return response.json()


async def async_fetch_authorized_github_user(aiohttp_session: ClientSession) -> Any:
    """Asynchronously fetches and returns the current authorized GitHub user.
    Uses the aiohttp module.
    """
    async with aiohttp_session.get(API_USER_URL, headers=HEADERS) as response:
        response_body = await response.json()
        return response_body
