from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.__base import Base


class Conservante(Base):

    __tablename__ = 'conservantes'

    nome: Mapped[str] = mapped_column(String(45), unique=True)
    descricao: Mapped[str] = mapped_column(String(45))

    def __repr__(self):
        return f'<Conservante: {self.nome}>'
