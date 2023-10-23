from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session
from typing import Union

from ca_app import (
    database,
    repository,
    schemas,
)


app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/events/{name}/questions/", response_model=schemas.Question, status_code=status.HTTP_201_CREATED)
def create_question(
    name: str, question: schemas.QuestionCreate, db: Session = Depends(database.get_db)
):
    return repository.create_event_question(db=db, question=question, name=name)


@app.get("/events/{name}", response_model=schemas.Event)
def read_event(name: str, db: Session = Depends(database.get_db)):
    db_event = repository.get_event_by_name(db, name=name)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
