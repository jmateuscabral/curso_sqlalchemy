from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.__base import Base


class Ingrediente(Base):

    __tablename__ = 'ingredientes'

    nome: Mapped[str] = mapped_column(String(45), unique=True)

    # picoles: Mapped[List['Picole']] = relationship(secondary='ingredientes_picole', back_populates='ingredientes')

    picoles: Mapped[List['Picoles']] = relationship(secondary='ingredientes_picole', backref='ingredientes')

    def __repr__(self):
        return f'<Ingrediente: {self.nome}>'
