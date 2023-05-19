"""Schemas for validating data from Blackboard API.

The extra fields are allowed since we only care about certain
fields, but the API will return more data.
"""
from pydantic import BaseModel, Extra


class NameBase(BaseModel):
    given: str
    family: str

    class Config:
        extra = Extra.allow


class UserBase(BaseModel):
    # We trust that userName is the OU email address handle.
    userName: str
    name: NameBase

    class Config:
        extra = Extra.allow


class MembershipItemBase(BaseModel):
    id: str
    userId: str
    user: UserBase
    courseRoleId: str

    class Config:
        extra = Extra.allow


# The result return from Blackboard API.
class MembershipResultBase(BaseModel):
    results: list[MembershipItemBase]

    class Config:
        extra = Extra.allow
