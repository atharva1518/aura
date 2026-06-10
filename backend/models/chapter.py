from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class Chapter(Base, BaseModel):
    __tablename__ = "chapters"

    curriculum_subject_id = Column(
        UUID(as_uuid=True),
        ForeignKey("curriculum_subjects.id"),
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    difficulty = Column(Integer)

    estimated_hours = Column(Integer)

    curriculum_subject = relationship(
        "CurriculumSubject",
        back_populates="chapters"
    )

    topics = relationship(
        "Topic",
        back_populates="chapter"
    )
    resources = relationship(
    "Resource",
    back_populates="chapter"
)
    quizzes = relationship(
    "Quiz",
    back_populates="chapter"
)