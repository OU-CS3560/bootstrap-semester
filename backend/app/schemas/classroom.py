from datetime import datetime

from pydantic import BaseModel, HttpUrl


# Common properties for inbound data to API.
class ClassroomBase(BaseModel):
    name: str
    begin_date: datetime
    end_date: datetime


class ClassroomCreate(ClassroomBase):
    github_classroom_link: HttpUrl | None = None


class ClassroomUpdate(ClassroomBase):
    name: str | None = None
    begin_date: datetime | None = None
    end_date: datetime | None = None
    github_classroom_link: HttpUrl | None = None


# Common properties for both DB and API.
class ClassroomInDBBase(ClassroomBase):
    id: int
    github_classroom_link: str

    class Config:
        orm_mode = True


# Additional properties to return via API.
class Classroom(ClassroomInDBBase):
    pass


# Additional properties to store in DB.
class ClassroomInDB(ClassroomInDBBase):
    pass
