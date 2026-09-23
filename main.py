"""Command-line interface entry point for the Task Manager application."""

from task_manager import TaskManager
from ai_service import create_simple_tasks


def print_menu() -> None:
    """Display the interactive command menu."""
    print("\nTask Manager Application")
    print("1. Add Task")
    print("2. Add Complex Task with AI")
    print("3. List Tasks")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit\n")


def main() -> None:
    """Run the main CLI interactive loop."""
    manager = TaskManager()

    while True:
        print_menu()

        try:
            choice = input("Choose an option: ").strip()

            match choice:
                case "1":
                    task = input("Enter the task description: ").strip()
                    if task:
                        manager.add_task(task)
                    else:
                        print("Task description cannot be empty.")
                case "2":
                    task = input("Enter the complex task description: ").strip()
                    if not task:
                        print("Task description cannot be empty.")
                        continue
                    subtasks = create_simple_tasks(task)
                    for subtask in subtasks:
                        if not subtask.startswith("Error"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break
                case "3":
                    manager.list_tasks()
                case "4":
                    task_id_str = input("Enter the task ID to complete: ").strip()
                    if task_id_str.isdigit():
                        manager.complete_task(int(task_id_str))
                    else:
                        print("Invalid task ID. Please enter a positive integer.")
                case "5":
                    task_id_str = input("Enter the task ID to delete: ").strip()
                    if task_id_str.isdigit():
                        manager.delete_task(int(task_id_str))
                    else:
                        print("Invalid task ID. Please enter a positive integer.")
                case "6":
                    print("Exiting the application.")
                    break
                case _:
                    print("Invalid option. Please enter a number between 1 and 6.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting the application.")
            break
        except ValueError as err:
            print(f"Invalid input: {err}")


if __name__ == "__main__":
    main()