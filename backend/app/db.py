from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    return engine
