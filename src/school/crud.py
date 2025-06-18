from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, EmailStr 
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from .models import School

school = APIRouter(prefix='/school')

class SchoolSchema(BaseModel):
    name: str
    email: EmailStr


@school.get("/", status_code=200)
def get_all(db: Session = Depends(get_db)) :
    all_school =  db.query(School).all()
    return all_school

@school.get("{id}")
def get(id: int, db: Session = Depends(get_db)):
    
    school = db.query(School).get(id)
    return school
     


@school.post("/add_school", status_code=201)
def post(item: SchoolSchema, db: Session = Depends(get_db)) -> JSONResponse:
    new = School(**item.dict())
  
    db.add(new)
    db.commit()
    return JSONResponse({"msg": "School Added"})



