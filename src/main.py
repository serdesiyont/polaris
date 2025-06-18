from fastapi import FastAPI
from db import engine, Base
from school import school


app = FastAPI()

app.include_router(school)

# Create tables for all models
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "Hello, Polaris!"}
