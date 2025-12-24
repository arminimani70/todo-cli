import json
import os


# ---------- Task ----------

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["id"],
            data["title"],
            data["completed"]
        )


# ---------- Task Manager ----------

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []

    def load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            data = json.load(file)
            self.tasks = [Task.from_dict(item) for item in data]

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(
                [task.to_dict() for task in self.tasks],
                file,
                indent=4
            )

    def _generate_id(self):
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, title):
        new_id = self._generate_id()
        task = Task(new_id, title)
        self.tasks.append(task)

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def mark_task_done(self, task_id):
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task.mark_done()
        return True

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True


# ---------- UI Helpers ----------

def show_menu():
    print("\n--- TO DO MENU ---")
    print("1. Add a new task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    return input("Choose an option: ").strip()


def show_tasks(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    for task in tasks:
        status = "Done" if task.completed else " "
        print(f"{task.id}. {task.title} [{status}]")


def get_valid_id(prompt):
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Please enter a number.")
            continue

        if user_input == "0":
            return 0

        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid number.")


# ---------- Main ----------

def main():
    manager = TaskManager("tasks.json")
    manager.load()

    while True:
        choice = show_menu()

        if choice == "1":
            title = input("Enter your task: ").strip()
            if not title:
                print("Task title cannot be empty.")
                continue

            manager.add_task(title)

        elif choice == "2":
            show_tasks(manager.tasks)

        elif choice == "3":
            if not manager.tasks:
                print("Task list is empty.")
                continue

            show_tasks(manager.tasks)
            task_id = get_valid_id("Enter task ID to mark as done (0 = exit): ")

            if task_id == 0:
                continue

            if manager.mark_task_done(task_id):
                print("Task marked as done.")
            else:
                print("Task not found.")

        elif choice == "4":
            if not manager.tasks:
                print("Task list is empty.")
                continue

            show_tasks(manager.tasks)
            task_id = get_valid_id("Enter task ID to delete (0 = exit): ")

            if task_id == 0:
                continue

            if manager.delete_task(task_id):
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            manager.save()
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
