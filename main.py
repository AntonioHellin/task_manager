from task_manager import TaskManager

def print_menu():
    print("\nTask Manager Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit\n")

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
                    manager.list_tasks()
                case "3":
                    task_id = int(input("Enter the task ID to complete: "))
                    manager.complete_task(task_id)
                case "4":
                    task_id = int(input("Enter the task ID to delete: "))
                    manager.delete_task(task_id)
                case "5":
                    print("Exiting the application.")
                    break
                case _:
                    print("Invalid option. Please try again.")
        except ValueError:
            print(f"Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()