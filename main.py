from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import database
import models

app = FastAPI()  

models.Base.metadata.create_all(bind=database.engine)
 
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Task(BaseModel):
    id: int
    title: str
    completed: bool

@app.get("/")
def root():
    return {"message": "Task Management API is running"}


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@app.post("/tasks")
def create_task(task: Task, db: Session = Depends(get_db)):
    new_task = models.Task(
        id=task.id,
        title=task.title,
        completed=task.completed
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task