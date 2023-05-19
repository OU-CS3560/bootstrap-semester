from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from ..main import app, get_db
from ..models import Base

SQLALCHEMY_DATABASE_URL_TEMPALTE = "sqlite+{driver}:///./test.db"

# So we are not dealing with asyncio in the pytest.
sync_engine = create_engine(
    SQLALCHEMY_DATABASE_URL_TEMPALTE.format(driver="pysqlite"),
    echo=True,
    connect_args={"check_same_thread": False},
)
Base.metadata.create_all(bind=sync_engine)
sync_engine.dispose()


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL_TEMPALTE.format(driver="aiosqlite"),
    echo=True,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = async_sessionmaker(
    bind=engine, autocommit=False, autoflush=False, expire_on_commit=False
)


async def override_get_db() -> AsyncSession:
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        await db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


def test_crud_classrooms():
    # This goes first for the empty list of classrooms.
    response = client.get("/classrooms/")
    assert response.status_code == 200
    assert response.json() == []

    # Create a classroom.
    response = client.post(
        "/classrooms/",
        json={
            "name": "CS3560 Spring 2022-2023",
            "begin_date": "2023-01-01T00:00-0400",
            "end_date": "2023-05-05T00:00-0400",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "end_date": "2023-05-05T00:00:00",
        "name": "CS3560 Spring 2022-2023",
        "begin_date": "2023-01-01T00:00:00",
        "github_classroom_link": None,
    }

    # This goes first for the empty list of classrooms.
    response = client.get("/classrooms/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "end_date": "2023-05-05T00:00:00",
            "name": "CS3560 Spring 2022-2023",
            "begin_date": "2023-01-01T00:00:00",
            "github_classroom_link": None,
        }
    ]
