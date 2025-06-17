from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from db import Base


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    resources: Mapped[str] = mapped_column(String, nullable=False)
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id"))
    school: Mapped["School"] = relationship(back_populates="posts")
    progress: Mapped[List["Progress"]] = relationship(back_populates="post")

