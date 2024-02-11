from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from .models import Driver
from .database import SessionLocal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your Django frontend URL
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


def making_response(code, msg, limit, offset, drivers):
    response = {
        "code": code,
        "msg": msg,
        "limit": limit,
        "offset": offset,
        "records": drivers
    }
    return response

@app.get("/")
async def read_root():
    return {"message": "Hello World :)"}

@app.get("/drivers/")
async def read_drivers(db: db_dependency, max_score: float = None, min_score: float = None, start_date: str = None,
                       end_date: str = None, limit: int = Query(default=100, gt=0, le=150),
                       offset: int = Query(default=0, gt=-1)):
    query = db.query(Driver)
    if max_score:
        query = query.filter(Driver.driving_score <= max_score)
    if min_score:
        query = query.filter(Driver.driving_score >= min_score)
    if start_date and end_date:
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            query = query.filter(Driver.updated_at.between(start_date, end_date))
        except ValueError:
            return JSONResponse(content=making_response(2, "Date format is not correct", limit, offset, []),
                                status_code=422)
    drivers = query.offset(offset).limit(limit).all()
    if drivers:
        return making_response(0, "Success", limit, offset, drivers)
    return making_response(1, "Success but no driver found.", limit, offset, [])
