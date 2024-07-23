class TodoList:
    def __init__(self):
        self.tasks = []
    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f"Completed task: {self.tasks[task_number]['task']}")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number.")
def main():
    todo_list = TodoList()
    while True:
        print("\n1.List of Tasks")
        print("2. Add Task")
        print("3. complete Task")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            todo_list.list_tasks()
        elif choice == "2":
            task = input("Enter the task:")
            todo_list.add_task(task)
        elif choice == "3":
            task_number = int(input("Enter the task number to complete: "))
            todo_list.complete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()