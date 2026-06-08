from sqlalchemy import Column, Integer, ForeignKey

from database.db import Base


class UserSubject(Base):
    __tablename__ = "user_subjects"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id")
    )