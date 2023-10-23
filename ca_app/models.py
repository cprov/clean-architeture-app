from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import (
    declarative_base,
    relationship,
)


from ca_app import schemas


Base = declarative_base()


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    questions = relationship("Question", back_populates="event")


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    event_id = Column(Integer, ForeignKey("event.id"))

    event = relationship("Event", back_populates="questions")
