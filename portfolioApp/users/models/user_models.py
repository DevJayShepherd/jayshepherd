from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from portfolioApp.core.db.base_class import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass