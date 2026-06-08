from sqlalchemy import Column, Integer, String, ForeignKey

from database.db import Base


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)

    chapter_id = Column(
        Integer,
        ForeignKey("chapters.id")
    )

    name = Column(String, nullable=False)