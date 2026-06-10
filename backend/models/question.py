from sqlalchemy import Column, Text, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class Question(Base, BaseModel):
    __tablename__ = "questions"

    quiz_id = Column(
        UUID(as_uuid=True),
        ForeignKey("quizzes.id"),
        nullable=False
    )

    topic_id = Column(
        UUID(as_uuid=True),
        ForeignKey("topics.id"),
        nullable=False
    )

    question_text = Column(Text)

    option_a = Column(Text)
    option_b = Column(Text)
    option_c = Column(Text)
    option_d = Column(Text)

    correct_option = Column(
        String(1)
    )

    quiz = relationship(
        "Quiz",
        back_populates="questions"
    )

    attempts = relationship(
        "QuestionAttempt",
        back_populates="question"
    )