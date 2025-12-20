import json
import os


# ---------- File Operations ----------

def load_tasks(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return json.load(file)


def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


# ---------- UI ----------

def show_menu():
    print("\n--- TO DO MENU ---")
    print("1. Add a new task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    return input("Choose an option: ").strip()


# ---------- Core Functions ----------

def add_task():
    title = input("Enter your task: ").strip()
    return title


def show_tasks(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else " "
        print(f'{task["id"]}. {task["title"]} [{status}]')


def mark_task_done(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    show_tasks(tasks)

    while True:
        user_input = input("Enter task ID to mark as done (0 = exit): ").strip()

        if not user_input:
            print("Please enter a number.")
            continue

        if user_input == "0":
            break

        try:
            task_id = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        found = False
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print("Task marked as done.")
                found = True
                break

        if found:
            break
        else:
            print("Task not found.")


def delete_task(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    while True:
        show_tasks(tasks)
        user_input = input("Enter task ID to delete (0 = exit): ").strip()

        if not user_input:
            print("Please enter a number.")
            continue

        if user_input == "0":
            break

        try:
            task_id = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        new_tasks = [task for task in tasks if task["id"] != task_id]

        if len(new_tasks) == len(tasks):
            print("Task not found.")
        else:
            tasks[:] = new_tasks
            print("Task deleted.")


# ---------- Main ----------

def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        choice = show_menu()

        if choice == "1":
            title = add_task()
            if not title:
                print("Task title cannot be empty.")
                continue

            if not tasks:
                new_id = 1
            else:
                new_id = max(task["id"] for task in tasks) + 1

            task = {
                "id": new_id,
                "title": title,
                "completed": False
            }

            tasks.append(task)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            mark_task_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks, filename)
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
