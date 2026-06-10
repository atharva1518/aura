from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class CurriculumSubject(Base, BaseModel):
    __tablename__ = "curriculum_subjects"

    subject_id = Column(
        UUID(as_uuid=True),
        ForeignKey("subjects.id"),
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

    __table_args__ = (
        UniqueConstraint(
            "subject_id",
            "board_id",
            "grade_id",
            name="uq_curriculum_subject"
        ),
    )

    subject = relationship(
        "Subject",
        back_populates="curriculum_subjects"
    )

    board = relationship(
        "Board",
        back_populates="curriculum_subjects"
    )

    grade = relationship(
        "Grade",
        back_populates="curriculum_subjects"
    )