import secrets

from sqlalchemy.orm import Session

from portfolioApp.apps.link_shortner.models.link_models import URL
from portfolioApp.apps.link_shortner.utils.linkzee_utils import generate_secret_key


def link_create(url: str, db: Session):
    try:
        key = generate_secret_key(length=5)
        secret_key = generate_secret_key(length=8)

        url_to_submit = URL(key=key, secret_key=secret_key, target_url=url)
        db.add(url_to_submit)
        db.commit()
        db.refresh(url_to_submit)

        url_to_submit.url = key
        url_to_submit.admin_url = secret_key

        return url_to_submit
    except Exception as e:
        print(e)
        return Exception


def get_link_db(url_key: str, db: Session):
    link = db.query(URL).filter(URL.key == url_key).first()
    if link:
        link.clicks += 1
        db.commit()

    return link
