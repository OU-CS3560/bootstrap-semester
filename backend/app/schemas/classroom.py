from typing import Optional
from datetime import datetime, date

from pydantic import validator, BaseModel, HttpUrl


# Common properties for inbound data to API.
class ClassroomBase(BaseModel):
    name: str
    begin_date: date
    end_date: date

    @validator("name")
    def name_must_not_be_empty(cls, val):
        if len(val.strip()) == 0:
            raise ValueError("must not be empty")
        return val


class ClassroomCreate(ClassroomBase):
    github_classroom_link: Optional[HttpUrl] = None

    @validator("github_classroom_link", pre=True, always=False)
    def validate_github_classroom_link(cls, val):
        if val == "":
            return None
        return val


class ClassroomUpdate(ClassroomBase):
    name: str
    begin_date: date
    end_date: date
    github_classroom_link: Optional[HttpUrl] = None

    @validator("github_classroom_link", pre=True, always=False)
    def validate_github_classroom_link(cls, val):
        if val == "":
            return None
        return val


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
