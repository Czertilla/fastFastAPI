from pydantic import BaseModel, ConfigDict
from uuid import uuid4, UUID


class TaskAdd(BaseModel):
    name: str
    description: str | None = None

class Task(TaskAdd):
    ID: UUID

    model_config = ConfigDict(from_attributes=True)


class TaskAddResponse(BaseModel):
    ok: bool = True
    task_id: UUID
