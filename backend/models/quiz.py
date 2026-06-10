from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class Quiz(Base, BaseModel):
    __tablename__ = "quizzes"

    chapter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("chapters.id"),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    quiz_type = Column(
        String(50)
    )

    chapter = relationship(
        "Chapter",
        back_populates="quizzes"
    )

    questions = relationship(
        "Question",
        back_populates="quiz"
    )

    attempts = relationship(
        "QuizAttempt",
        back_populates="quiz"
    )