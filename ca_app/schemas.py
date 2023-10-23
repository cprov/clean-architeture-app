from pydantic import (
    BaseModel,
    ConfigDict,
)


class QuestionBase(BaseModel):
    content: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    model_config = ConfigDict(from_attributes = True)

    id: int


class EventBase(BaseModel):
    name: str


class Event(EventBase):
    model_config = ConfigDict(from_attributes = True)

    questions: list[Question] = []
