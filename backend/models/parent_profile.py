from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class ParentProfile(Base, BaseModel):
    __tablename__ = "parent_profiles"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    full_name = Column(String(255), nullable=False)

    phone = Column(String(20))

    occupation = Column(String(100))

    user = relationship("User")

    student_links = relationship(
        "StudentParentLink",
        back_populates="parent"
    )