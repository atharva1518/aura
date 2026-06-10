from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class QuestionAttempt(Base, BaseModel):
    __tablename__ = "question_attempts"

    attempt_id = Column(
        UUID(as_uuid=True),
        ForeignKey("quiz_attempts.id"),
        nullable=False
    )

    question_id = Column(
        UUID(as_uuid=True),
        ForeignKey("questions.id"),
        nullable=False
    )

    is_correct = Column(Boolean)

    attempt = relationship(
        "QuizAttempt",
        back_populates="question_attempts"
    )

    question = relationship(
        "Question",
        back_populates="attempts"
    )