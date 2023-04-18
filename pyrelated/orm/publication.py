from __future__ import annotations

from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from pyrelated.orm.base import Base


class Publication(Base):
    __tablename__ = "publications"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    year: Mapped[Optional[int]]
    abstract: Mapped[Optional[str]]
    type_bibtex_publication = mapped_column(String(30))
    pages_from: Mapped[Optional[int]]
    pages_to: Mapped[Optional[int]]
    gscholar_bibref: Mapped[Optional[str]]
    arxiv_versions: Mapped[List["ArxivPub"]] = relationship(
        "ArxivPub", back_populates="publication"
    )

    def __repr__(self) -> str:
        return f"Publication(id={self.id!r}, title={self.title!r}, year={self.year!r})"


class ArxivPub(Base):
    __tablename__ = "arxiv_pubs"

    identifier: Mapped[str] = mapped_column(primary_key=True)
    publication_id: Mapped[int] = mapped_column(ForeignKey("publications.id"))
    publication: Mapped["Publication"] = relationship(
        "Publication", back_populates="arxiv_versions", foreign_keys=[publication_id]
    )
