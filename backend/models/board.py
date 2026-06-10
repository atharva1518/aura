from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class Board(Base, BaseModel):
    __tablename__ = "boards"

    name = Column(
        String(50),
        unique=True,
        nullable=False
    )

    student_profiles = relationship(
        "StudentProfile",
        back_populates="board"
    )

    curriculum_subjects = relationship(
        "CurriculumSubject",
        back_populates="board"
    )