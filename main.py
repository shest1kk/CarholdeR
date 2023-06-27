from fastapi import FastAPI

import models.models
from config import engine
from UserRouter import UsersRouter
from RolesRouter import RolesRouter

from fastapi.middleware.cors import CORSMiddleware

models.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://172.16.191.119:8080",
    "http://localhost:8080",
    "http://127.0.0.1:8080/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RolesRouter, prefix='/roles', tags=['ROLES'])
app.include_router(UsersRouter, prefix='/users', tags=['USERS'])
