
from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas


# Create a todo
def create_todo(
    db: Session,
    todo: schemas.TodoCreate,
    owner_id: int
):
    new_todo = models.Todo(
        task_name=todo.task_name,
        due_date=todo.due_date,
        status=todo.status,
        owner_id=owner_id
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


# Read all todos belonging to a user
def get_todos(db: Session, owner_id: int):
    return (
        db.query(models.Todo)
        .filter(models.Todo.owner_id == owner_id)
        .all()
    )


# Read one todo
def get_todo(db: Session, todo_id: int, owner_id: int):
    todo = (
        db.query(models.Todo)
        .filter(
            models.Todo.id == todo_id,
            models.Todo.owner_id == owner_id
        )
        .first()
    )

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


# Update a todo
def update_todo(
    db: Session,
    todo_id: int,
    todo_data: schemas.TodoUpdate,
    owner_id: int
):
    todo = get_todo(db, todo_id, owner_id)

    changes = todo_data.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)

    return todo


# Delete a todo
def delete_todo(
    db: Session,
    todo_id: int,
    owner_id: int
):
    todo = get_todo(db, todo_id, owner_id)

    db.delete(todo)
    db.commit()

    return {"message": "Todo deleted successfully"}