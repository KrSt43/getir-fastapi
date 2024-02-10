from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from .models import Driver
from .database import SessionLocal

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
async def read_drivers(db: db_dependency):
    query = db.query(Driver)
    drivers = query.all()
    return drivers

