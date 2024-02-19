from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from portfolioApp.core.db.database import database
from portfolioApp.core.settings import settings
from portfolioApp.apps.link_shortner.router.api_router import link_short_router
from portfolioApp.users.router.api_router import user_router
from portfolioApp.core.db.database import Base, engine

from portfolioApp.apps.link_shortner.models import link_models


def include_router(app):
    app.include_router(link_short_router)
    app.include_router(user_router)


def start_application():
    app = FastAPI(title=settings.APP_NAME)

    origins = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app)

    return app


app = start_application()


@app.on_event("startup")
async def startup():
    print('Starting the database...')
    Base.metadata.create_all(bind=engine)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    print('Shutting down the database...')
    await database.disconnect()


@app.get("/")
async def root():
    return {"message": "Hello World"}
