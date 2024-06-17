from datetime import datetime

class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.completed = False
        self.due_date = due_date

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        if self.due_date:
            due_date_str = self.due_date.strftime('%Y-%m-%d %I:%M %p')  # Format to 12-hour with AM/PM
            return f"{self.description} (Due: {due_date_str}) - {status}"
        else:
            return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Task '{description}' added to your to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task '{self.tasks[index].description}' marked as completed.")
        else:
            print("Invalid index.")

    def edit_task_description(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
            print(f"Task '{new_description}' updated successfully.")
        else:
            print("Invalid index.")

    def edit_task_due_date(self, index, new_due_date):
        if 0 <= index < len(self.tasks):
            self.tasks[index].due_date = new_due_date
            print(f"Due date for task '{self.tasks[index].description}' updated to {new_due_date}.")
        else:
            print("Invalid index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.description}' removed from your to-do list.")
        else:
            print("Invalid index.")

# Function to display a menu and capture user input
def display_menu():
    print("\n\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Edit Task Description")
    print("5. Edit Task Due Date")
    print("6. Remove Task")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    return choice

# Function to get a valid date input from user
def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d %I:%M %p')
            return date_obj
        except ValueError:
            print("Invalid date format. Please enter date in format YYYY-MM-DD hh:mm AM/PM")

# Main program loop
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        choice = display_menu()

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            due_date = get_date_input("Enter due date (optional, format: YYYY-MM-DD hh:mm AM/PM): ")
            todo_list.add_task(description, due_date)
        elif choice == '3':
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '4':
            index = int(input("Enter the index of the task to edit: ")) - 1
            new_description = input("Enter new description: ")
            todo_list.edit_task_description(index, new_description)
        elif choice == '5':
            index = int(input("Enter the index of the task to edit: ")) - 1
            new_due_date = get_date_input("Enter new due date (format: YYYY-MM-DD hh:mm AM/PM): ")
            todo_list.edit_task_due_date(index, new_due_date)
        elif choice == '6':
            index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '7':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
