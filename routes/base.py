from fastapi import APIRouter
from fastapi.responses import Response
from markdown2 import Markdown

router = APIRouter()


@router.get("/", response_class=Response)
def index() -> Response:
    """Returns the demo.md and README.md as an HTML page to the base endpoint."""
    with open("./README.md", "rb") as readme, open("./views/demo.md", "rb") as urls:
        readme_html = Markdown().convert(urls.read() + readme.read())
        return Response(readme_html, media_type="text/html")
