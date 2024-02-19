from fastapi import APIRouter
from portfolioApp.apps.link_shortner.router.v1.link_short_routes import link_short_router

linkzee_router = APIRouter()


# add the link short router below by including them
linkzee_router.include_router(link_short_router, tags=['link shortner routes'], prefix='/linkzee')