from pydantic import BaseModel


class HelloWorldResponse(BaseModel):
    payload: str


class GitHubResponse(BaseModel):
    user_name: str
    followers: int
    repo_count: int
