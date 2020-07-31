from fastapi import APIRouter, FastAPI

from routes import base, example


def get_app() -> FastAPI:
    """Creates and returns FastAPI app with routes attached"""
    app = FastAPI()

    # Add base route at localhost:8000
    app.include_router(base.router)

    # Add additional routes under localhost:8000/api
    app.include_router(get_router(), prefix="/api")
    return app


def get_router() -> APIRouter:
    """Creates router that will contain additional routes under localhost:8000/api"""
    router = APIRouter()

    # Example route
    router.include_router(example.router, prefix="/example")
    return router


# Starts FastAPI app
app = get_app()
