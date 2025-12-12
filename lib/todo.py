class Todo:

    def __init__(self, task):
        self.task = task
        self.complete = False
    # task: string
    # initially incomplete


    def mark_complete(self):
        self.complete = True
    # marks the task as complete

    def is_complete(self):
        return self.complete

    