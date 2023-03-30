from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.__base import Base


class TipoPicole(Base):

    __tablename__ = 'tipos_picole'

    nome: Mapped[str] = mapped_column(String(45), unique=True)

    tipo_picole: Mapped[List['Lote']] = relationship(back_populates='tipo_picole')

    # lote_id: Mapped[int] = mapped_column(ForeignKey("lotes.id"))
    # user: Mapped["Lote"] = relationship(back_populates="tipos_picole")

    def __repr__(self):
        return f'<Tipo Picole: {self.nome}>'
