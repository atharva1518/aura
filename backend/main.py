from fastapi import FastAPI

from database.db import engine, Base

from models.user import User
from models.subject import Subject
from models.user_subject import UserSubject
from models.chapter import Chapter
from models.topics import Topic

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Aura Backend Running"}