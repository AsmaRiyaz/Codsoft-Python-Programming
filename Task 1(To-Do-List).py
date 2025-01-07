import json

# File to store the to-do list data
TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from the file."""
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task to the to-do list."""
    task = input("Enter the task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {task['status']}")

def update_task():
    """Update the status of a task."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to update.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_status = input("Enter new status (Pending/Completed): ").capitalize()
            if new_status in ["Pending", "Completed"]:
                tasks[task_number - 1]["status"] = new_status
                save_tasks(tasks)
                print("Task status updated successfully!")
            else:
                print("Invalid status. Please enter 'Pending' or 'Completed'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Delete a task from the to-do list."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            confirm = input(f"Are you sure you want to delete task {task_number}? (yes/no): ").lower()
            if confirm == "yes":
                tasks.pop(task_number - 1)
                save_tasks(tasks)
                print("Task deleted successfully!")
            else:
                print("Task deletion canceled.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    """Main menu for the To-Do List application."""
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
