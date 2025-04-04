from task import Task
from task_status import TaskStatus
from user import User
from collections import defaultdict

class TaskManager:
    _instance = None

    def __init__(self):
        if TaskManager._instance is not None:
            raise Exception("This is a Singleton class")
        self.tasks = {}  # task_id -> Task
        self.user_tasks = defaultdict(list)  # user -> List[Task]

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TaskManager()
        return cls._instance

    def create_task(self, id, title, description, priority, due_date, user: User):
        if id in self.tasks:
            raise Exception("Task ID already exists")
        
        task = Task(id, title, description, priority, due_date)
        task.set_user(user)
        
        self.tasks[id] = task
        self.user_tasks[user].append(task)
        user.add_task(task)

        print(f"Task '{title}' created and assigned to {user.name}")
        return task

    def update_task(self, task_id, user: User, title, description, priority, due_date):
        task = self.tasks.get(task_id)
        if not task:
            raise Exception("Task not found")

        if task.get_user() != user:
            raise Exception("User does not own this task")

        task.set_title(title)
        task.set_description(description)
        task.set_priority(priority)
        task.set_due_date(due_date)
        print(f"Task {task_id} updated by {user.name}")

    def remove_task(self, task_id, user: User):
        task = self.tasks.get(task_id)
        if not task:
            raise Exception("Task not found")

        if task.get_user() != user:
            raise Exception("User does not own this task")

        user.remove_task(task)
        self.user_tasks[user].remove(task)
        del self.tasks[task_id]

        print(f"Task {task_id} removed by {user.name}")

    def assign_task(self, from_user: User, to_user: User, task_id: int):
        task = self.tasks.get(task_id)
        if not task:
            raise Exception("Task not found")

        if task.get_user() != from_user:
            raise Exception("Only the current owner can assign the task")

        from_user.remove_task(task)
        to_user.add_task(task)
        task.set_user(to_user)

        self.user_tasks[from_user].remove(task)
        self.user_tasks[to_user].append(task)

        print(f"Task {task_id} reassigned from {from_user.name} to {to_user.name}")

    def mark_as_completed(self, task_id: int, user: User):
        task = self.tasks.get(task_id)
        if not task:
            raise Exception("Task not found")

        if task.get_user() != user:
            raise Exception("User is not authorized to complete this task")

        task.status = TaskStatus.COMPLETED
        print(f"Task {task_id} marked as completed by {user.name}")
