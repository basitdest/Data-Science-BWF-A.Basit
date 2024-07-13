# Problem Statement
# Create a simple to-do list manager using Python. 
# The system will allow users to add, view, update, and delete tasks.
tasks = []
def add_task(description, due_date):
    task = {"description": description, "due_date": due_date}
    tasks.append(task)
    print(f"Task '{description}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['description']} - Due Date: {task['due_date']}")

def update_task(task_id, new_description, new_due_date):
    if task_id <= 0 or task_id > len(tasks):
        print("Invalid task ID.")
        return
    tasks[task_id - 1] = {"description": new_description, "due_date": new_due_date}
    print(f"Task {task_id} updated successfully!")

def delete_task(task_id):
    if task_id <= 0 or task_id > len(tasks):
        print("Invalid task ID.")
        return
    removed_task = tasks.pop(task_id - 1)
    print(f"Task '{removed_task['description']}' deleted successfully!")

def save_tasks_to_file(filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['description']},{task['due_date']}\n")
    print(f"Tasks saved to '{filename}'.")

def load_tasks_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                description, due_date = line.strip().split(',')
                add_task(description, due_date)
        print(f"Tasks loaded from '{filename}'.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
def main():
    while True:
        print("\nPersonal To-Do List Manager")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Save tasks to file")
        print("6. Load tasks from file")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(description, due_date)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            update_task(task_id, new_description, new_due_date)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            save_tasks_to_file(filename)
        elif choice == '6':
            filename = input("Enter filename to load tasks: ")
            load_tasks_from_file(filename)
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
