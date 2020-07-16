from fastapi import APIRouter, FastAPI

from routes import test


def get_router() -> APIRouter:
    router = APIRouter()
    router.include_router(test.router, prefix="/test")
    return router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(get_router(), prefix="/api")
    return app


app = get_app()
