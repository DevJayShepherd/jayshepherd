import re

from urllib.parse import urlparse

from sqlalchemy import Column, String, DATETIME
from sqlalchemy.orm import validates
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from portfolioApp.core.db.base_class import Base


class Link(Base):
    __tablename__ = 'links'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    original_url = Column(String, nullable=False)
    shortened_path = Column(String, unique=True, nullable=False)
    created_at = Column(DATETIME(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

    @validates('original_url')
    def validate_url(self, key, url):
        parsed = urlparse(url)
        if bool(parsed.netloc) and bool(parsed.scheme):
            return url
        else:
            raise ValueError("Invalid URL")

    @validates('shortened_path')
    def validate_path(self, key, path):
        if not bool(re.match("^[a-zA-Z0-9_-]*$", path)):
            raise ValueError("Path can only contain alphanumeric characters, hyphens and underscores")
        return path
