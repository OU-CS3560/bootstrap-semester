"""Collection of Create, Read, Update and Delete Operations."""
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas
from . import models


async def create_classroom(db: AsyncSession, classroom: schemas.ClassroomCreate):
    classroom_data = classroom.dict()
    db_obj = models.Classroom(**classroom_data)
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def get_classrooms(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(models.Classroom).offset(skip).limit(limit)
    results = await db.execute(query)
    rows = results.scalars().all()
    return rows
