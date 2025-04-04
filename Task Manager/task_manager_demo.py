from task_manager import TaskManager
from user import User
from task import Task
from datetime import datetime

class TaskManagerDemo:
    def run():
        task_manager = TaskManager.get_instance()

        #Create Users
        mayur = User(1, "Mayur", "abc@gmail.com")
        kirtan = User(2, "Kirtan", "xyz@gmail.com")
        shreyas = User(3, "Shreyas", "lmn@gmail.com")

        #Create a Task
        task_1 = task_manager.create_task(1, "Task-1", "Description-1", 1, datetime.now(), mayur)
        task_2 = task_manager.create_task(2, "Task-2", "Description-2", 1, datetime.now(), kirtan)

        #Update a task
        task_manager.update_task(1, mayur, "Task-1", "Updated_Task_1_Description", 2, datetime.now())

        #Assign a task
        print(f"{task_2.user.name}")
        task_manager.assign_task(kirtan, shreyas, 2)
        print(f"{task_2.user.name}")

        task_manager.mark_as_completed(1, mayur)

if __name__ == "__main__":
    TaskManagerDemo.run()