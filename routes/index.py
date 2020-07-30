from fastapi import APIRouter
from fastapi.responses import Response
from markdown2 import Markdown

router = APIRouter()


@router.get("/", response_class=Response)
def get() -> Response:
    """Returns the README.md and urls.md as an HTML page to the base endpoint."""
    with open("./README.md", "rb") as readme, open("./views/urls.md", "rb") as urls:
        readme_html = Markdown().convert(readme.read() + urls.read())
        return Response(readme_html, media_type="text/html")
