"""Test cases for simple model creation and usage."""
from datetime import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models import *


@pytest.fixture
def in_memory_engine_with_tables():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    Base.metadata.create_all(bind=engine)

    return engine


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
