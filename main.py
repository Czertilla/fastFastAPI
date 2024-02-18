from fastapi import FastAPI
from schemas import *

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as task_router


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print("база очищ")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
