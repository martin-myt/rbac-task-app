from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def create_task(db: Session, task: TaskCreate, user_id: str) -> Task:
    db_task = Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status=task.status,
        assigned_user_id=task.assigned_user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[Task]:
    return db.query(Task).offset(skip).limit(limit).all()


def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task_id: int, task: TaskUpdate) -> Optional[Task]:
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return None
    
    for field, value in task.dict(exclude_unset=True).items():
        setattr(db_task, field, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int) -> bool:
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return False
    
    db.delete(db_task)
    db.commit()
    return True 