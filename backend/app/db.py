import asyncio

from sqlalchemy import inspect
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


async def create_tables_if_not_exist():
    from .models import Base

    async with engine.connect() as conn:
        # inspect() does not work in async.
        tables = await conn.run_sync(
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )

        if len(tables) == 0:
            print("[db]: database has no tables. Assume an empty database and will be creating all tables")
            # create_all() does not work in async.
            await conn.run_sync(Base.metadata.create_all)
            await conn.commit()
        else:
            print("[db]: database is not empty. skipping tables creation")

if __name__ == "__main__":
    asyncio.run(create_tables_if_not_exist())
