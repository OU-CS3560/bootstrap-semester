"""Collection of Create, Read, Update and Delete Operations."""
from sqlalchemy.orm import Session

from . import schemas
from . import models


def create_classroom(db: Session, classroom: schemas.ClassroomCreate):
    classroom_data = classroom.dict()
    db_obj = models.Classroom(**classroom_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_classrooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Classroom).offset(skip).limit(limit).all()
