class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def list_tasks(self):
        if self.tasks:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks.")

    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            print(f"Task '{task}' marked as complete.")
            del self.tasks[index - 1]
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            print(f"Task '{task}' deleted.")
            del self.tasks[index - 1]
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark as complete: "))
            todo_list.complete_task(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting Todo List.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()