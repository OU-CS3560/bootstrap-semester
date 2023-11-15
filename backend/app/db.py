from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from .config import settings

if settings.sqlalchemy_database_url.startswith("sqlite"):
    engine = create_async_engine(
        settings.sqlalchemy_database_url,
        echo=True,
        connect_args={"check_same_thread": False},
    )
elif settings.sqlalchemy_database_url.startswith("postgres"):
    engine = create_async_engine(
        settings.sqlalchemy_database_url,
        echo=True,
    )
SessionLocal = async_sessionmaker(
    bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
)
