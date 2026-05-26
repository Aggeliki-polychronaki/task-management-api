from fastapi import FastAPI, Depends, HTTPException
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

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    return task