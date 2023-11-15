"""
Test cases for simple model creation and usage.

These tests directly interact with the models and not
does not deal with the app's endpoints.
"""
from datetime import datetime

import pytest
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models import *


@pytest.fixture
def in_memory_engine_with_tables():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    Base.metadata.create_all(bind=engine)

    return engine


@pytest.fixture
def a_classroom():
    return Classroom(
        name="cs3560-s22-23",
        begin_date=datetime(year=2023, month=1, day=10),
        end_date=datetime(year=2023, month=5, day=5),
    )


@pytest.fixture
def list_of_students(a_classroom):
    result = [
        Student(
            first_name="Bob",
            last_name="Cat",
            username="bobcat",
            github_username="bobcat",
            classroom=a_classroom,
        )
    ]
    return result


class TestClassroom:
    def test_creation(self, in_memory_engine_with_tables):
        with Session(in_memory_engine_with_tables) as session:
            c = Classroom(
                name="cs3560-s22-23",
                begin_date=datetime(year=2023, month=1, day=10),
                end_date=datetime(year=2023, month=5, day=5),
            )
            session.add(c)
            session.commit()

            # begin_date and end_date are required.
            with pytest.raises(IntegrityError):
                c = Classroom(
                    name="cs3560-s22-23",
                )
                session.add(c)
                session.commit()

    def test_deletion(self, in_memory_engine_with_tables, a_classroom):
        with Session(in_memory_engine_with_tables) as session:
            session.add(a_classroom)
            session.commit()

            # Minimal student creation.
            # without github username and team
            s = Student(
                first_name="Bob",
                last_name="Cat",
                username="bobcat",
                classroom=a_classroom,
            )
            session.add(s)
            session.commit()

            s = Student(
                first_name="Bob",
                last_name="Cat",
                username="bobcat",
                github_username="bobcat",
                classroom=a_classroom,
            )
            session.add(s)
            session.commit()

            # Delete the classroom.
            session.delete(a_classroom)
            session.commit()

            # The two student objects should also be deleted.
            result = session.execute(select(func.count()).select_from(Student))
            assert result.one()[0] == 0


class TestStudentModel:
    def test_creation(self, in_memory_engine_with_tables, a_classroom):
        with Session(in_memory_engine_with_tables) as session:
            session.add(a_classroom)
            session.commit()

            # Minimal student creation.
            # without github username and team
            s = Student(
                first_name="Bob",
                last_name="Cat",
                username="bobcat",
                classroom=a_classroom,
            )
            session.add(s)
            session.commit()

            s = Student(
                first_name="Bob",
                last_name="Cat",
                username="bobcat",
                github_username="bobcat",
                classroom=a_classroom,
            )
            session.add(s)
            session.commit()


class TestMilestoneModel:
    def test_milestone(self, in_memory_engine_with_tables, a_classroom):
        with Session(in_memory_engine_with_tables) as session:
            session.add(a_classroom)
            session.commit()

            m = Milestone(
                name="Checkpoint 1",
                begin_date=datetime(year=2023, month=1, day=1),
                end_date=datetime(year=2023, month=1, day=14),
                classroom=a_classroom,
            )
            session.add(m)
            session.commit()
