from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.__base import Base


class AditivoNutritivo(Base):

    __tablename__ = 'aditivos_nutritivos'

    nome: Mapped[str] = mapped_column(String(45), unique=True)
    formula_quimica: Mapped[str] = mapped_column(String(45), unique=True)

    def __repr__(self):
        return f'<Aditivo Nutritivo: {self.nome}>'
