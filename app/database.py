from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import setting


# from app.config import setting


def get_db():
    db = seesion_local()
    try:
        yield db
    finally:
        db.close()


SQL_ALCHEMY_DATABASE_URL = f"mysql+mysqldb://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
seesion_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
