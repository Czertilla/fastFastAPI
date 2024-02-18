from sqlalchemy import select
from database import new_session, TaskORM
from schemas import TaskAdd, Task
from uuid import uuid4


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> uuid4:
        async with new_session() as session:
            task_dict = data.model_dump()
            task_dict.update({"ID": uuid4()})
            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.ID

    @classmethod
    async def find_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [Task.model_validate(task_model) for task_model in task_models]
            return task_schemas