from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from db import Base

class School(Base):
    __tablename__ = "schools"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    students: Mapped[List["Student_List"]] = relationship(back_populates="school")
    posts: Mapped[List["Post"]] = relationship(back_populates="school")

class Student_List(Base):
    __tablename__ = "student_list"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id"))
    school: Mapped["School"] = relationship(back_populates="students")
    progress: Mapped[List["Progress"]] = relationship(back_populates="student")

