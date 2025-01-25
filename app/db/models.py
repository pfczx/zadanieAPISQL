from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import UUID, uuid4

class Task(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: str = Field(default="brak opisu", max_length=500)
    status: str = Field(default="do wykonania")

class PomodoroSession(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    start_time: datetime
    end_time: datetime
    duration: int = Field(default=25)
    completed: bool = Field(default=False)