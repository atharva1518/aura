from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class StudentProfile(Base, BaseModel):
    __tablename__ = "student_profiles"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    board_id = Column(
        UUID(as_uuid=True),
        ForeignKey("boards.id"),
        nullable=False
    )

    grade_id = Column(
        UUID(as_uuid=True),
        ForeignKey("grades.id"),
        nullable=False
    )

    full_name = Column(
        String(255),
        nullable=False
    )

    school_name = Column(
        String(255)
    )

    target_score = Column(
        Integer
    )

    daily_study_hours = Column(
        Integer
    )

    exam_date = Column(
        Date
    )

    user = relationship(
        "User",
        back_populates="student_profile"
    )

    board = relationship(
        "Board",
        back_populates="student_profiles"
    )

    grade = relationship(
        "Grade",
        back_populates="student_profiles"
    )
    
    user_subjects = relationship(
    "UserSubject",
    back_populates="student"
)
    study_plans = relationship(
    "StudyPlan",
    back_populates="student"
)

quiz_attempts = relationship(
    "QuizAttempt",
    back_populates="student"
)
parent_links = relationship(
    "StudentParentLink",
    back_populates="student"
)