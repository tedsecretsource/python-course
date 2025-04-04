from os import getenv
from typing import Any, Generator

from sqlmodel import Session, create_engine

engine = create_engine(getenv("POSTGRES_URL"))

def get_db_session() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session
