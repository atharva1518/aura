from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class Grade(Base, BaseModel):
    __tablename__ = "grades"

    grade_number = Column(
        Integer,
        unique=True,
        nullable=False
    )

    student_profiles = relationship(
        "StudentProfile",
        back_populates="grade"
    )

    curriculum_subjects = relationship(
        "CurriculumSubject",
        back_populates="grade"
    )