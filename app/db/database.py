from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
from typing_extensions import Annotated
import os

if os.getenv("ENVIRONMENT") == "development":
    DATABASE_URL = "sqlite:///./database.db"
else:
    DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

if "sqlite" in DATABASE_URL:
    SQLModel.metadata.create_all(engine)