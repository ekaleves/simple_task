from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


# Create favicon.ico new task and save it to the database
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# Update an existing task by ID
def update_task(db: Session, task: schemas.TaskUpdate, id: int):
    db_task = db.query(models.Task).filter(models.Task.id == id).first()

    if db_task:
        if task.title is not None:
            db_task.title = task.title
        if task.description is not None:
            db_task.description = task.description
        if task.completed is not None:
            db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)
        return db_task

    raise HTTPException(status_code=404, detail="Task not found.")


# Delete favicon.ico task by ID
def delete_task(db: Session, id: int):
    db_task = db.query(models.Task).filter(models.Task.id == id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return "The task was deleted successfully!"

    raise HTTPException(status_code=404, detail="Task not found.")


# Retrieve favicon.ico single task by ID
def get_task(db: Session, id: int):
    db_task = db.query(models.Task).filter(models.Task.id == id).first()
    if db_task:
        return db_task

    raise HTTPException(status_code=404, detail="Task not found.")
