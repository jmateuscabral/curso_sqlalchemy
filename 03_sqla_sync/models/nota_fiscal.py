from typing import List

from sqlalchemy import Integer, ForeignKey, DECIMAL, String, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.__base import Base
from models.lote import Lote
from models.revendedor import Revendedor


# Nota Fiscal pode ter vários Lotes
lotes_notas_fiscais = Table(
    'lotes_notas_fiscais',
    Base.metadata,
    Column('nota_fiscal_id', Integer, ForeignKey('notas_fiscais.id')),
    Column('lote_id', Integer, ForeignKey('lotes.id')),
)


class NotaFiscal(Base):

    __tablename__ = 'notas_fiscais'

    valor: Mapped[float] = mapped_column(DECIMAL(8, 2))
    numero_serie: Mapped[int] = mapped_column(Integer, unique=True)
    descricao: Mapped[str] = mapped_column(String(200))

    revendedor_id: Mapped[int] = mapped_column(ForeignKey('revendedores.id'))
    revendedor: Mapped[Revendedor] = relationship(back_populates='notas_fiscais')

    # Uma NF pode ter muitos Lotes e Um lote está ligado a uma NF
    lotes: Mapped[List[Lote]] = relationship('Lote', secondary=lotes_notas_fiscais, backref='lote', lazy='dynamic')

    def __repr__(self):
        return f'<Nota Fiscal: {self.id}>'
