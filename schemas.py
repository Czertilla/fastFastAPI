from pydantic import BaseModel
from uuid import uuid4, UUID


class TaskAdd(BaseModel):
    name: str
    description: str | None = None

class Task(TaskAdd):
    ID: UUID


class TaskAddResponse(BaseModel):
    ok: bool = True
    task_id: UUID