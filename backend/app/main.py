from typing import Union
from datetime import datetime

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud
from .schemas import MembershipResultBase, ClassroomCreate
from .models import Base
from .db import SessionLocal, engine


def get_db_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}


@app.get("/classrooms/")
async def get_classrooms(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)
):
    return crud.get_classrooms(db, skip, limit)


@app.post("/classrooms/")
async def create_classroom(
    classroom: ClassroomCreate, db: Session = Depends(get_db_session)
):
    db_obj = crud.create_classroom(db, classroom)
    return db_obj


@app.post("/students/import")
async def import_students(
    membership_results: MembershipResultBase, db: Session = Depends(get_db_session)
):
    pass
