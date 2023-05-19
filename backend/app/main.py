from typing import Union

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseSettings

from . import crud
from .config import settings
from .schemas import MembershipResultBase, ClassroomCreate
from .db import SessionLocal, engine


async def get_db() -> AsyncSession:
    try:
        db = SessionLocal()
        yield db
    finally:
        await db.close()


app = FastAPI()


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}


@app.get("/classrooms/")
async def get_classrooms(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    return await crud.get_classrooms(db, skip, limit)


@app.post("/classrooms/")
async def create_classroom(
    classroom: ClassroomCreate, db: AsyncSession = Depends(get_db)
):
    db_obj = await crud.create_classroom(db, classroom)
    return db_obj


@app.post("/students/import")
async def import_students(
    membership_results: MembershipResultBase, db: AsyncSession = Depends(get_db)
):
    pass
