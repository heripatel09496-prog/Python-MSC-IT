
from datetime import date
from pydantic import BaseModel, ConfigDict


class UserSignup(BaseModel):
    username: str
    password: str
    full_name: str


class UserOut(BaseModel):
    id: int
    username: str
    full_name: str

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class TodoCreate(BaseModel):
    task_name: str
    due_date: date
    status: bool = False


class TodoUpdate(BaseModel):
    task_name: str | None = None
    due_date: date | None = None
    status: bool | None = None


class TodoOut(BaseModel):
    id: int
    task_name: str
    due_date: date
    status: bool

    model_config = ConfigDict(from_attributes=True)