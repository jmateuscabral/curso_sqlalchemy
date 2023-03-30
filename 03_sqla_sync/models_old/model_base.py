import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


# ModelBase = declarative_base()

class ModelBase(declarative_base()):

    __abstract__ = True
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
