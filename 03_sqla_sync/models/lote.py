from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.__base import Base

from models.tipo_picole import TipoPicole


class Lote(Base):

    __tablename__ = 'lotes'

    tipo_picole_id: Mapped[int] = mapped_column(ForeignKey('tipos_picole.id'))
    tipo_picole: Mapped[TipoPicole] = relationship(back_populates='lotes')

    quantidade: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f'<Tipo Embalagem: {self.id}>'
