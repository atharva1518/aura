from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func

from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    grade = Column(String)

    board = Column(String)

    target_score = Column(Integer)

    daily_study_hours = Column(Integer)

    exam_date = Column(Date)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )