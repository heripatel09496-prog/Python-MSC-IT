
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import models
import schemas
import crud
import auth

from database import Base, engine, SessionLocal

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Todo App with JWT")


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Find currently logged-in user
def get_current_user(
    username: str = Depends(auth.get_current_username),
    db: Session = Depends(get_db)
):
    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Home
@app.get("/")
def read_root():
    return {"message": "Welcome to Todo App"}


# Signup
@app.post(
    "/signup",
    response_model=schemas.UserOut,
    status_code=status.HTTP_201_CREATED
)
def signup(
    user: schemas.UserSignup,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(models.User)
        .filter(models.User.username == user.username)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = models.User(
        username=user.username,
        password_hash=auth.hash_password(user.password),
        full_name=user.full_name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Login
@app.post("/login", response_model=schemas.TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = (
        db.query(models.User)
        .filter(
            models.User.username == form_data.username
        )
        .first()
    )

    if (
        user is None
        or not auth.verify_password(
            form_data.password,
            user.password_hash
        )
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    token = auth.create_access_token(user.username)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# Protected profile
@app.get("/profile", response_model=schemas.UserOut)
def get_profile(
    current_user: models.User = Depends(get_current_user)
):
    return current_user


# READ: Get all todos for the logged-in user
@app.get("/todos", response_model=list[schemas.TodoOut])
def read_todos(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_todos(db, current_user.id)


# READ: Get one todo
@app.get("/todos/{todo_id}", response_model=schemas.TodoOut)
def read_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_todo(db, todo_id, current_user.id)


# CREATE: Add a todo
@app.post(
    "/todos",
    response_model=schemas.TodoOut,
    status_code=status.HTTP_201_CREATED
)
def add_todo(
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_todo(db, todo, current_user.id)


# UPDATE: Edit a todo
@app.put("/todos/{todo_id}", response_model=schemas.TodoOut)
def edit_todo(
    todo_id: int,
    todo: schemas.TodoUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.update_todo(
        db, todo_id, todo, current_user.id
    )


# DELETE: Remove a todo
@app.delete("/todos/{todo_id}")
def remove_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.delete_todo(
        db, todo_id, current_user.id
    )