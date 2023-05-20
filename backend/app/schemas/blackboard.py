"""Schemas for validating data from Blackboard API.

The extra fields are allowed since we only care about certain
fields, but the API will return more data.
"""
from pydantic import BaseModel, Extra


class Name(BaseModel):
    given: str
    family: str

    class Config:
        extra = Extra.allow


class User(BaseModel):
    # We trust that userName is the OU email address handle.
    userName: str
    name: Name

    class Config:
        extra = Extra.allow


class MembershipItem(BaseModel):
    id: str
    userId: str
    user: User
    courseRoleId: str

    class Config:
        extra = Extra.allow


# The result return from Blackboard API.
class MembershipResult(BaseModel):
    results: list[MembershipItem]

    class Config:
        extra = Extra.allow
