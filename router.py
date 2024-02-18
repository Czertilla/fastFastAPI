from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository

from schemas import Task, TaskAdd, TaskAddResponse

router = APIRouter(
    prefix="/tasks",
    tags= ["Tasks"]
)

@router.post("")
async def add_task(
    task: Annotated[TaskAdd, Depends()]
) -> TaskAddResponse:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all()
    return tasks