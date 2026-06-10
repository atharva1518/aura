from fastapi import FastAPI

from database.db import engine, Base

# Import all models so SQLAlchemy registers them
import models

app = FastAPI()


# Create all tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Aura Backend Running"}
