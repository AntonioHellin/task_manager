class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.description}"

class TaskManager:

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Added task: {description}")

    def list_tasks(self):
        if not self._tasks:
            print("No tasks available.")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Completed task: {task.description}")
                return
        print(f"Task with ID {id} not found.")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Deleted task: {task.description}")
                return
        print(f"Task with ID {id} not found.")
