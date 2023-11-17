from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    full_name: str | None = None
    disabled: bool | None = None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int


class UserInDB(UserInDBBase):
    hashed_password: str


class User(UserInDBBase):
    pass
