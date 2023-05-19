from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

engine = create_async_engine(
    "sqlite+aiosqlite:///:memory:", echo=True, connect_args={"check_same_thread": False}
)
SessionLocal = async_sessionmaker(
    bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
)
