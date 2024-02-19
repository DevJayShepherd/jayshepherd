import validators
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from portfolioApp.apps.link_shortner.crud.linkzee_crud import link_create, get_link_db
from portfolioApp.apps.link_shortner.schemas.link_schema import URLBase, URLInfo
from portfolioApp.core.db.database import get_db

link_short_router = APIRouter()


@link_short_router.post('/new', response_model=URLInfo)
async def create_new_link(url: URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="Invalid URL...")

    details = link_create(url.target_url, db)
    return details


@link_short_router.get("/{url_key}")
def forward_to_target_url(url_key: str, request: Request, db: Session = Depends(get_db)):
    link = get_link_db(url_key, db)
    if link:
        return RedirectResponse(link.target_url)
    else:
        raise HTTPException(status_code=404, detail="Link not found...")
