from task_status import TaskStatus
class Task:
    def __init__(self, id, title, description, priority, due_date, task_status: TaskStatus = TaskStatus.PENDING):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = task_status
        self.user = None
    
    def set_user(self, user):
        self.user = user
    
    def remove_user(self, user):
        self.user = None
    
    def get_user(self):
        return self.user
    
    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title
    
    def set_description(self, description):
        self.description = description
    
    def set_priority(self, priority):
        self.priority = priority
    
    def set_due_date(self, due_date):
        self.due_date = due_date