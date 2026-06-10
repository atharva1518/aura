from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class StudyTask(Base, BaseModel):
    __tablename__ = "study_tasks"

    plan_id = Column(
        UUID(as_uuid=True),
        ForeignKey("study_plans.id"),
        nullable=False
    )

    chapter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("chapters.id"),
        nullable=False
    )

    title = Column(String(255))

    estimated_minutes = Column(Integer)

    status = Column(String(20))

    plan = relationship(
        "StudyPlan",
        back_populates="tasks"
    )