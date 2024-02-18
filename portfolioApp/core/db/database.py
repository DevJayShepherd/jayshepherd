import databases

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
