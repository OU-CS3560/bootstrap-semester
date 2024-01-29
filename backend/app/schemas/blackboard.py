"""Schemas for validating data from Blackboard API.

The extra fields are allowed since we only care about certain
fields, but the API will return more data.
"""
from pydantic import BaseModel


class Name(BaseModel):
    given: str
    family: str

    model_config = {"extra": "allow"}


class User(BaseModel):
    # We trust that userName is the OU email address handle.
    userName: str
    name: Name

    model_config = {"extra": "allow"}


class MembershipItem(BaseModel):
    id: str
    userId: str
    user: User
    courseRoleId: str

    model_config = {"extra": "allow"}


# The result return from Blackboard API.
class MembershipResult(BaseModel):
    results: list[MembershipItem]

    model_config = {"extra": "allow"}
