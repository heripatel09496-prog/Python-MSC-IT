
from sqlalchemy import (
    Column, Integer, String, Boolean, Date, ForeignKey
)
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=False)


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(150), nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(Boolean, default=False, nullable=False)

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )