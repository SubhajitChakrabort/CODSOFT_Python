import sys

class TodoList:
    def __init__(self):
        self.tasks = [] 

    def add_task(self):
        task = input("Enter a new task: ").strip()
        if not task:
            print("Task cannot be empty.")
            return
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def update_task(self):
        self.view_tasks()
        try:
            task_index = int(input("Enter the task number to update: ")) - 1
            if task_index < 0 or task_index >= len(self.tasks):
                print("Invalid task number.")
                return
            new_task = input(f"Enter the new description for task {task_index + 1}: ").strip()
            if not new_task:
                print("Task description cannot be empty.")
                return
            self.tasks[task_index] = new_task
            print(f"Task {task_index + 1} updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_index = int(input("Enter the task number to delete: ")) - 1
            if task_index < 0 or task_index >= len(self.tasks):
                print("Invalid task number.")
                return
            deleted_task = self.tasks.pop(task_index)
            print(f"Task '{deleted_task}' deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print()

    def show_menu(self):
        print("\nTodo List Menu")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.update_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.view_tasks()
            elif choice == '5':
                print("Exiting Todo List. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.run()
