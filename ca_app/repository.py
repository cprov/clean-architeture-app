from sqlalchemy.orm import Session


from ca_app import (
    models,
    schemas,
)


def get_event_by_name(db: Session, name: str):
    return db.query(models.Event).filter(models.Event.name == name).first()


def create_event_question(db: Session, question: schemas.QuestionCreate, name: str):
    db_event = get_event_by_name(db, name)
    if db_event is None:
        db_event = models.Event(name=name)
        db.add(db_event)
        db.commit()
        db.refresh(db_event)

    db_question = models.Question(**question.model_dump(), event_id=db_event.id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
