from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.__base import Base


class Sabor(Base):

    __tablename__ = 'sabores'

    nome: Mapped[str] = mapped_column(String(45), unique=True)

    def __repr__(self):
        return f'<Sabor: {self.nome}>'
