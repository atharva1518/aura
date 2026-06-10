from sqlalchemy import Column, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class Progress(Base, BaseModel):
    __tablename__ = "progress"

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student_profiles.id"),
        nullable=False
    )

    curriculum_subject_id = Column(
        UUID(as_uuid=True),
        ForeignKey("curriculum_subjects.id"),
        nullable=False
    )

    completion_percent = Column(
        Numeric(5, 2)
    )

    accuracy_percent = Column(
        Numeric(5, 2)
    )