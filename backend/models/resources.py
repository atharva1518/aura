from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class Resource(Base, BaseModel):
    __tablename__ = "resources"

    chapter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("chapters.id"),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    resource_type = Column(
        String(20),
        nullable=False
    )

    resource_url = Column(Text)

    uploaded_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    chapter = relationship(
        "Chapter",
        back_populates="resources"
    )