from fastapi import FastAPI

import models
import database
from routers import tasks

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Task Management API is running"}