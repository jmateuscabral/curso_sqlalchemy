import sqlalchemy as sa

from sqlalchemy.orm import Session, sessionmaker

from pathlib import Path  # No SQLite
from typing import Optional

from sqlalchemy.future.engine import Engine


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine | None:
    """
    Função para configurar a conexão com o Banco de Dados
    """

    global __engine

    if __engine:
        return

    if sqlite:

        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'

        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={'check_same_thread': False})

    else:
        # conn_str = f'postgresql://geek:university@localhost:5432/picoles'
        conn_str = f'postgresql://postgres:@localhost:5432/picoles'
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função para criar a sessão com o Banco de Dados
    """

    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_tables() -> None:

    global __engine

    if not __engine:
        create_engine(True)

    from models.__base import Base
    from models import __all__models

    Base.metadata.drop_all(__engine)
    Base.metadata.create_all(__engine)

