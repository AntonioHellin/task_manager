from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
    print("\nTask Manager Application")
    print("1. Add Task")
    print("2. Add complex task with AI")
    print("3. List Tasks")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit\n")

def main():

    manager = TaskManager()

    while True:
        print_menu()

        try:
            choice = input("Choose an option: ")

            match choice:
                case "1":
                    task = input("Enter the task description: ")
                    manager.add_task(task)
                case "2":
                    task = input("Enter the complex task description: ")
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
                    task_id = int(input("Enter the task ID to complete: "))
                    manager.complete_task(task_id)
                case "5":
                    task_id = int(input("Enter the task ID to delete: "))
                    manager.delete_task(task_id)
                case "6":
                    print("Exiting the application.")
                    break
                case _:
                    print("Invalid option. Please try again.")
        except ValueError:
            print(f"Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()