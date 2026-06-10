import uuid

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.db import Base
from models.base_model import BaseModel


class User(Base, BaseModel):
    __tablename__ = "users"

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )

    role = Column(
        String(20),
        default="student"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    student_profile = relationship(
        "StudentProfile",
        back_populates="user",
        uselist=False
    )