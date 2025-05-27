class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append({"description": task_description, "completed": False})

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "[✅]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['description']}")

    def mark_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Show Tasks")
            print("2. Add Task")
            print("3. Mark Task as Complete")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                self.show_tasks()
            elif choice == "2":
                task = input("Enter task description: ")
                self.add_task(task)
            elif choice == "3":
                self.show_tasks()
                try:
                    num = int(input("Enter task number to mark complete: "))
                    self.mark_complete(num)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                print("Exiting to-do list. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    todo = ToDoList()
    todo.run()