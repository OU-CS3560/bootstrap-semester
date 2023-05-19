from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.models import *

if __name__ == "__main__":
    engine = create_engine("sqlite+pysqlite:///./backend.copy.db", echo=True)
    Base.metadata.create_all(bind=engine)

    session = Session(engine)
