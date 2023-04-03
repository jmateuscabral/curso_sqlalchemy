from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.__base import Base


class Revendedor(Base):

    __tablename__ = 'revendedores'

    cnpj: Mapped[str] = mapped_column(String(45), unique=True)
    razao_social: Mapped[str] = mapped_column(String(100))
    contato: Mapped[str] = mapped_column(String(45))

    def __repr__(self):
        return f'<Revendedor: {self.contato}>'
