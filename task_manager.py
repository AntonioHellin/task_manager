"""Core Task and TaskManager entities for local task tracking."""

import json
from typing import List, Optional


class Task:
    """Represents an individual task item."""

    def __init__(self, id: int, description: str, completed: bool = False):
        """Initialize a new task item.

        Args:
            id: Unique numeric identifier.
            description: Task title or details.
            completed: Completion status flag.
        """
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        """Format task for console display."""
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.description}"


class TaskManager:
    """Manages tasks with JSON-backed persistence."""

    FILENAME = "tasks.json"

    def __init__(self):
        """Initialize TaskManager and load existing tasks from disk."""
        self._tasks: List[Task] = []
        self._next_id: int = 1
        self.load_tasks()

    def add_task(self, description: str) -> Task:
        """Add a new task with auto-incremented ID.

        Args:
            description: Description of the task.

        Returns:
            The created Task instance.
        """
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Added task: {description}")
        self.save_tasks()
        return task

    def list_tasks(self) -> None:
        """Print all current tasks to the console."""
        if not self._tasks:
            print("No tasks available.")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id: int) -> bool:
        """Mark a task as completed by ID.

        Args:
            id: Task ID to mark completed.

        Returns:
            True if task found and updated, False otherwise.
        """
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Completed task: {task.description}")
                self.save_tasks()
                return True
        print(f"Task with ID {id} not found.")
        return False

    def delete_task(self, id: int) -> bool:
        """Remove a task from the list by ID.

        Args:
            id: Task ID to delete.

        Returns:
            True if task found and deleted, False otherwise.
        """
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Deleted task: {task.description}")
                self.save_tasks()
                return True
        print(f"Task with ID {id} not found.")
        return False

    def load_tasks(self) -> None:
        """Load tasks from the JSON storage file."""
        try:
            with open(self.FILENAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    task = Task(item["id"], item["description"], item["completed"])
                    self._tasks.append(task)
                    self._next_id = max(self._next_id, task.id + 1)
        except (FileNotFoundError, json.JSONDecodeError):
            self._tasks = []

    def save_tasks(self) -> None:
        """Persist current task list to JSON storage file."""
        try:
            with open(self.FILENAME, "w", encoding="utf-8") as file:
                json.dump([task.__dict__ for task in self._tasks], file, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
