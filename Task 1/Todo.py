class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return "[{}] {}".format("X" if self.completed else " ", self.description)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))
        print("Task added:", description)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            print("Task deleted:", self.tasks[index].description)
            del self.tasks[index]
        else:
            print("Invalid task index")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed:", self.tasks[index].description)
        else:
            print("Invalid task index")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print("{}. {}".format(i, task))

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")
