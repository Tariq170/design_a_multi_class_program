class TodoList:
    def __init__(self):
        self.task = []

    def add(self, todo):
        self.task.append(todo)
    # todo: instance of Todo

    def incomplete(self):
        return [tasks for tasks in self.tasks if not tasks.is_complete()]
    # returns list of tasks not completed

    def complete(self):
        return [tasks for tasks in self.tasks if tasks.is_complete()]
    # returns list of tasks completed    
