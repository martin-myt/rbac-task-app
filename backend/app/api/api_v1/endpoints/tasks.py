from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task import create_task, get_tasks, get_task_by_id, update_task, delete_task
from app.core.auth import get_current_user, require_role

router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create_task_endpoint(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return create_task(db=db, task=task, user_id=current_user["sub"])


@router.get("/", response_model=List[TaskResponse])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    tasks = get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_task = get_task_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task_endpoint(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_task = update_task(db=db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.delete("/{task_id}")
@require_role("manager")
def delete_task_endpoint(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    success = delete_task(db=db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"} 