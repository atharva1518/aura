from sqlalchemy import Column, Integer, String

from database.db import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    grade = Column(String)

    board = Column(String)