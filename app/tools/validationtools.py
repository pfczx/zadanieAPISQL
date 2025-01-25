from fastapi import HTTPException
from sqlmodel import Session, select
from app.db.database import engine
from app.db.models import Task, PomodoroSession


class TaskTools:
    statuses = ["do wykonania", "w trakcie", "zakończone", "do wykoania"]

    @staticmethod
    def task_crate_validator(title,description,status):
        with Session(engine) as session:
            if len(title) not in range(3,100):
                raise HTTPException(
                    status_code=404,detail="wrong title len"
                )
            if title is None:
                raise HTTPException(
                    status_code=404,detail="no title"
                )
            existing_task = session.exec(select(Task).where(Task.title == title)).first()
            if existing_task:
                    raise HTTPException(
                        status_code=404,detail="task with same title exists"
                    )
            if len(description) not in range(0,300):
                raise HTTPException(
                    status_code=404,detail="wrong description len"
                )
            if status not in TaskTools.statuses:
                raise HTTPException(
                    status_code=404,detail="wrong status"
                )
    @staticmethod
    def status_validator(status):
        if status not in TaskTools.statuses:
            raise HTTPException(
                status_code=404,detail="wrong status"
            )
    @staticmethod
    def task_by_id_validator(task_id):
        with Session(engine) as session:
            task = session.get(Task, task_id)
            if not task:
                raise HTTPException(status_code=404, detail="task not found")
            return task

class PomodoroTools:
    @staticmethod
    def pomodoro_create_validator(task_id):
        with Session(engine) as session:
            active_pomodoro = session.exec(select(PomodoroSession).where(PomodoroSession.id == task_id).where(PomodoroSession.completed == False)).first()
            if active_pomodoro:
                raise HTTPException(status_code=400, detail="pomodoro timer is already active for this task")
    @staticmethod
    def pomodoro_stopper_validator(task_id):
        with Session(engine) as session:
            active_pomodoro = session.exec(select(PomodoroSession).where(PomodoroSession.id == task_id).where(PomodoroSession.completed == False)).first()
            if not active_pomodoro:
                raise HTTPException(status_code=400, detail="no active pomodoro timer for this task")




