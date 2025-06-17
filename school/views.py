from pydantic import BaseModel
from fastapi import APIRouter, Depends
from .models import School
from db import Base, get_db
from sqlalchemy.orm import Session
school = APIRouter(prefix="/sch")

class SchoolModel(BaseModel):
    name: str

@school.get("/")
async def home(db: Session = Depends(get_db)):
    al = db.query(School).all()
    return al

@school.post("/add", status_code=201)
async def add(school: SchoolModel, db: Session = Depends(get_db)):
    new = School(name=school.name)
    db.add(new)
    db.commit()
    db.refresh(new)
    return {"msg": "yay"}