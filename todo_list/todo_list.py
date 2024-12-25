
def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to the list.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from the list.")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
