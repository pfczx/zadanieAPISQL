from fastapi import HTTPException


class TaskTools:
    statuses = ["do wykonania", "w trakcie", "zakończone", "do wykoania"]

    @staticmethod
    def task_crate_validator(title,description,status,task_list):
        if len(title) not in range(3,100):
            raise HTTPException(
                status_code=404,detail="wrong title len"
            )
        if title is None:
            raise HTTPException(
                status_code=404,detail="no title"
            )
        for item in task_list:
            if item["title"] == title:
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
    def task_by_id_validator(id_num,task_list):
        print(id_num)
        checker = False
        for task in task_list:
            print(f"id taska:{str(task['id'])},,,,,id podane:{str(id_num)}")
            if str(task["id"]) == str(id_num):
                checker = True
        if not checker:
            raise HTTPException(
                status_code=404,detail="wrong id"
            )

class PomodoroTools:
    @staticmethod
    def pomodoro_create_validator(task_id,pomodoro_list):
        if pomodoro_list == []:
            return
        else:
            for pomodoro in pomodoro_list:
                if str(task_id) == str(pomodoro["id"]):
                    if not pomodoro["completed"]:
                        raise HTTPException(
                            status_code=404,detail="pomodoro timer is active"
                        )
    @staticmethod
    def pomodoro_stopper_validator(task_id,pomodoro_list):
        for pomodoro in pomodoro_list:
            if str(task_id) == str(pomodoro["id"]):
                if pomodoro["completed"]:
                    raise HTTPException(
                        status_code=404,detail="pomodoro already completed"

                    )





