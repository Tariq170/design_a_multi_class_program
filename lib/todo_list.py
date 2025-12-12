class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, todo):
        self.tasks.append(todo)
    # todo: instance of Todo

    def incomplete(self):
        return [task for task in self.tasks if not task.is_complete]
    # returns list of tasks not completed

    def complete(self):
        return [task for task in self.tasks if task.is_complete]
    # returns list of tasks completed    
