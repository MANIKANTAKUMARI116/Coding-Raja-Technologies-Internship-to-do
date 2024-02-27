import os
import json
from datetime import datetime

# Function to load tasks from file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return {"tasks": []}

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks, name, priority, due_date):
    tasks["tasks"].append({
        "name": name,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d") if due_date else None,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks, index):
    if 0 <= index < len(tasks["tasks"]):
        del tasks["tasks"][index]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

# Function to mark a task as completed
def complete_task(tasks, index):
    if 0 <= index < len(tasks["tasks"]):
        tasks["tasks"][index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

# Function to display tasks
def display_tasks(tasks):
    if not tasks["tasks"]:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks["tasks"]):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i+1}. [{status}] {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter task priority (high/medium/low): ").lower()
            due_date_str = input("Enter due date (YYYY-MM-DD), press Enter for none: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            add_task(tasks, name, priority, due_date)
        elif choice == "2":
            display_tasks(tasks)
            index = int(input("Enter index of task to remove: ")) - 1
            remove_task(tasks, index)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter index of task to complete: ")) - 1
            complete_task(tasks, index)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
