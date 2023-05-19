from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from .config import settings

engine = create_async_engine(
    settings.sqlalchemy_database_url,
    echo=True,
    # FIXME(KC): This only apply to sqlite.
    connect_args={"check_same_thread": False},
)
SessionLocal = async_sessionmaker(
    bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
)
