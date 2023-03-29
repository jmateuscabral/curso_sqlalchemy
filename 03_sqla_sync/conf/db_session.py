import sqlalchemy as sa

from sqlalchemy.orm import Session, sessionmaker

from pathlib import Path  # No SQLite
from typing import Optional

from sqlalchemy.future.engine import Engine

# from models.model_base import ModelBase


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False):




