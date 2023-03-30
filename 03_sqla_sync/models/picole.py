from typing import List, Optional

from sqlalchemy import Integer, ForeignKey, DECIMAL, String, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.__base import Base
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole


ingredientes_picole = Table(
    'ingredientes_picole',
    Base.metadata,
    Column('ingrediente_id', ForeignKey('ingredientes.id')),
    Column('picole_id', ForeignKey('picoles.id')),
)


conservantes_picole = Table(
    'conservantes_picole',
    Base.metadata,
    Column('conservante_id', ForeignKey('conservantes.id')),
    Column('picole_id', ForeignKey('picoles.id')),
)


aditivos_nutritivos_picole = Table(
    'aditivos_nutritivos_picole',
    Base.metadata,
    Column('aditivo_nutritivo_id', ForeignKey('aditivos_nutritivos.id')),
    Column('picole_id', ForeignKey('picoles.id')),
)


class Picole(Base):

    __tablename__ = 'picoles'

    valor: Mapped[float] = mapped_column(DECIMAL(8, 2))

    id_sabor: Mapped[Sabor] = mapped_column(Integer, ForeignKey('sabores.id'))
    sabor: Mapped[Sabor] = relationship('Sabor', lazy='joined')

    id_tipo_embalagem: Mapped[Sabor] = mapped_column(Integer, ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: Mapped[TipoEmbalagem] = relationship('TipoEmbalagem', lazy='joined')

    id_tipo_picole: Mapped[TipoPicole] = mapped_column(Integer, ForeignKey('tipos_picole.id'))
    tipo_picole: Mapped[TipoPicole] = relationship('TipoPicole', lazy='joined')

    # Um picolé pode ter vários ingredientes
    ingredientes: Mapped[List[Ingrediente]] = relationship(
        'Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='joined')

    # Um picolé pode ter vários conservantes ou nenhum
    conervantes: Mapped[Optional[List[Conservante]]] = relationship(
        'Conservante', secondary=ingredientes_picole, backref='conservante', lazy='joined')

    # Um picolé pode ter vários aditivos nutritivos ou nenhum
    aditivos_nutritivos: Mapped[Optional[List[AditivoNutritivo]]] = relationship(
        'AditivoNutritivo', secondary=ingredientes_picole, backref='aditivo_nutritivo', lazy='joined')

    def __repr__(self):
        return f'<Picole: {self.id}>'
