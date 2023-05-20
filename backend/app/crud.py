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


async def get_classroom(db: AsyncSession, classroom_id: int):
    query = select(models.Classroom).where(models.Classroom.id == classroom_id)
    results = await db.execute(query)
    classroom = results.scalars().one()
    return classroom


async def import_students_bb(
    db: AsyncSession, classroom_id: int, import_data: schemas.MembershipResult
):
    classroom_db_obj = await get_classroom(db, classroom_id)

    db_objs = []
    for item in import_data.results:
        if (
            item.courseRoleId == "Instructor"
            or item.courseRoleId == "TeachingAssistant"
        ):
            continue

        obj_data = {
            "classroom": classroom_db_obj,
            "first_name": item.user.name.given,
            "last_name": item.user.name.family,
            "username": item.user.userName,
        }
        db_obj = models.Student(**obj_data)
        db_objs.append(db_obj)

    db.add_all(db_objs)
    await db.commit()
    return {"count": len(db_objs)}
