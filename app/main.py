from fastapi import FastAPI
from sqlmodel import SQLModel

from app.db.session import engine
from app.models.complaint import Complaint

app = FastAPI()


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)  # tymczasowo, dla dev/test


@app.get("/")
def read_root():
    return {"message": "Hello, SQLModel!"}
