#!/usr/bin/env python3

# Initialize an empty Todo list
todo_list = []

# Display welcome message
print("\t <<<=============================================>>>")
print("\n \t Welcome to Muhammad Talha - Todo-List Application \n")
print("\t <<<=============================================>>>")

def main():
    condition = True
    while condition:
        # Display menu options
        print("\nSelect an option you want to do:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. View Todo-List")
        print("5. Exit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            view_task()
        elif choice == "5":
            condition = False
            print("\nThank you for using the Todo-List application. Goodbye!")
        else:
            print("\nInvalid choice. Please try again.")

# Function to add a task to the Todo List
def add_task():
    new_task = input("\nEnter your new Task: ").strip()
    if new_task:
        todo_list.append(new_task)
        print(f"\n'{new_task}' has been added successfully to the Todo-List.")
    else:
        print("\nTask cannot be empty. Please try again.")

# Function to view all Todo List tasks
def view_task():
    if not todo_list:
        print("\nYour Todo List is empty.")
    else:
        print("\nYour Todo List:")
        index = 1
        for task in todo_list:
            print(f"{index}. {task}")
            index += 1

# Function to delete a task from the list
def delete_task():
    view_task()
    if todo_list:
        task_index = input("\nEnter the index number of the task you want to delete: ").strip()
        if task_index.isdigit() and 1 <= int(task_index) <= len(todo_list):
            deleted_task = todo_list.pop(int(task_index) - 1)
            print(f"\n'{deleted_task}' has been deleted successfully from your Todo-List.")
        else:
            print("\nInvalid index. Please enter a valid number.")

# Function to update a task in the Todo List
def update_task():
    view_task()
    if todo_list:
        task_index = input("\nEnter the index number of the task you want to update: ").strip()
        if task_index.isdigit() and 1 <= int(task_index) <= len(todo_list):
            new_task_name = input("Enter the new task name: ").strip()
            if new_task_name:
                todo_list[int(task_index) - 1] = new_task_name
                print(f"\nTask at index {task_index} has been updated successfully.")
            else:
                print("\nTask name cannot be empty. Please try again.")
        else:
            print("\nInvalid index. Please enter a valid number.")

# Run the program
main()
