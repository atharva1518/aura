from sqlalchemy import Column, Integer, String, ForeignKey

from database.db import Base


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id")
    )

    name = Column(String, nullable=False)

    difficulty = Column(Integer)

    estimated_hours = Column(Integer)