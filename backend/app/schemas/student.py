from pydantic import BaseModel


# Common properties for inbound data to the API.
class StudentBase(BaseModel):
    first_name: str
    last_name: str
    username: str


# Additional properties expected to be seen when Student is created.
class StudentCreate(StudentBase):
    github_username: str | None = None
    codewars_username: str | None = None


class StudentUpdate(StudentBase):
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    github_username: str | None = None
    codewars_username: str | None = None
    is_drop: bool | None = None
    note: str | None = None
