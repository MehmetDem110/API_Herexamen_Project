from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",  # Adjust this to match your Svelte app's domain
    # Add more domains as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/posts/", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post, user_id=user_id)

@app.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db=db, post_id=post_id, post=post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.delete_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.post("/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, post_id: int, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment, post_id=post_id)

@app.get("/comments/", response_model=list[schemas.Comment])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comments = crud.get_comments(db, skip=skip, limit=limit)
    return comments
