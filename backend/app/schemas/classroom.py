from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl, validator
from pydantic.functional_validators import AfterValidator, BeforeValidator
from typing_extensions import Annotated


def check_name(val):
    if len(val.strip()) == 0:
        raise ValueError("must not be empty")
    return val


def check_github_classroom_link(val):
    if val == "":
        return None
    return val


# Common properties for inbound data to API.
class ClassroomBase(BaseModel):
    name: Annotated[str, AfterValidator(check_name)]
    begin_date: date
    end_date: date


class ClassroomCreate(ClassroomBase):
    github_classroom_link: Annotated[
        Optional[HttpUrl],
        BeforeValidator(check_github_classroom_link),
        AfterValidator(lambda v: str(v) if v is not None else v),
    ] = None


class ClassroomUpdate(ClassroomBase):
    name: Optional[str] = None
    begin_date: Optional[date] = None
    end_date: Optional[date] = None
    github_classroom_link: Annotated[
        Optional[HttpUrl],
        BeforeValidator(check_github_classroom_link),
        AfterValidator(lambda v: str(v) if v is not None else v),
    ] = None


# Common properties for both DB and API.
class ClassroomInDBBase(ClassroomBase):
    id: int
    github_classroom_link: str

    model_config = {"from_attributes": True}


# Additional properties to return via API.
class Classroom(ClassroomInDBBase):
    pass


# Additional properties to store in DB.
class ClassroomInDB(ClassroomInDBBase):
    pass
