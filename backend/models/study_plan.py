from sqlalchemy import Column, Date, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class StudyPlan(Base, BaseModel):
    __tablename__ = "study_plans"

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student_profiles.id"),
        nullable=False
    )

    plan_date = Column(Date)

    status = Column(String(20))

    student = relationship(
        "StudentProfile",
        back_populates="study_plans"
    )

    tasks = relationship(
        "StudyTask",
        back_populates="plan"
    )