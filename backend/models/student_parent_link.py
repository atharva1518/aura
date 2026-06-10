from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class StudentParentLink(Base, BaseModel):
    __tablename__ = "student_parent_links"

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student_profiles.id"),
        nullable=False
    )

    parent_id = Column(
        UUID(as_uuid=True),
        ForeignKey("parent_profiles.id"),
        nullable=False
    )

    relationship_type = Column(
        String(50)
    )

    student = relationship(
        "StudentProfile",
        back_populates="parent_links"
    )

    parent = relationship(
        "ParentProfile",
        back_populates="student_links"
    )