from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from db import Base


class Progress(Base):
    __tablename__ = "progress"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    resources: Mapped[str] = mapped_column(String, nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey("student_list.id"))
    student: Mapped["Student_List"] = relationship(back_populates="progress")
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped["Post"] = relationship(back_populates="progress")

