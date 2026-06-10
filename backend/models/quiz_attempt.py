from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class QuizAttempt(Base, BaseModel):
    __tablename__ = "quiz_attempts"

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student_profiles.id"),
        nullable=False
    )

    quiz_id = Column(
        UUID(as_uuid=True),
        ForeignKey("quizzes.id"),
        nullable=False
    )

    score = Column(Integer)

    total_questions = Column(Integer)

    time_taken = Column(Integer)

    student = relationship(
        "StudentProfile",
        back_populates="quiz_attempts"
    )

    quiz = relationship(
        "Quiz",
        back_populates="attempts"
    )

    question_attempts = relationship(
        "QuestionAttempt",
        back_populates="attempt"
    )