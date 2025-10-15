import json

class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.description}"

class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Added task: {description}")
        self.save_tasks()

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
                self.save_tasks()
                return
        print(f"Task with ID {id} not found.")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Deleted task: {task.description}")
                self.save_tasks()
                return
        print(f"Task with ID {id} not found.")

    def load_tasks(self):
        try:
            with open(self.FILENAME, 'r') as file:
                data = json.load(file)
                for item in data:
                    task = Task(item['id'], item['description'], item['completed'])
                    self._tasks.append(task)
                    self._next_id = max(self._next_id, task.id + 1)
        except FileNotFoundError:
            self._tasks = []

    def save_tasks(self):
        try:
            with open(self.FILENAME, "w") as file:
                json.dump([task.__dict__ for task in self._tasks], file)
        except Exception as e:
            print(f"Error saving tasks: {e}")
