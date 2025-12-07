import json
import os

FILE_NAME = "todo_list.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\n===== Your To-Do List =====")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['task']} [{status}]")


def add_task(tasks):
    new_task = input("\nEnter new task: ")
    tasks.append({"task": new_task, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")


def mark_complete(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to mark complete: "))
        tasks[num-1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except:
        print("Invalid input!")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to delete: "))
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task deleted!")
    except:
        print("Invalid input!")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List Manager... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
