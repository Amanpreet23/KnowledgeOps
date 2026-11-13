from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import RegisterTortoise

from database.database_setup import TORTOISE_ORM
from routes.user_routes import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with RegisterTortoise(app, config=TORTOISE_ORM, generate_schemas=False):
        yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router, tags=["User"])