from task import Task

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.tasks = {}  # task_id -> Task

    def add_task(self, task: Task):
        self.tasks[task.get_id()] = task

    def remove_task(self, task: Task):
        if task.get_id() in self.tasks:
            del self.tasks[task.get_id()]

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id
