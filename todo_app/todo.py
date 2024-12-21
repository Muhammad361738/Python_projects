#!/usr/bin/env python3

todo_list = []
condition = True

# Print messages without using 'termcolor'
print("\t <<<=============================================>>>")
print("\n \t Welcome to Muhammad Talha - Todo-List Application \n")
print("\t <<<=============================================>>>")

def main():
    global condition
    while condition:
        # Display menu options
        print("\nSelect an option you want to do:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. View Todo-List")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

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
        else:
            print("\nInvalid choice. Please try again.")

# Function to add task to Todo List
def add_task():
    new_task = input("\nEnter your new Task: ")
    todo_list.append(new_task)
    print(f"\n{new_task} Task is added successfully in Todo-List")

# Function to view all Todo List tasks
def view_task():
    if not todo_list:
        print("\nYour Todo List is empty.")
    else:
        print("\nYour Todo List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

# Function to delete a task from the list
def delete_task():
    view_task()
    if todo_list:
        task_index = input("\nEnter the index number of the Task you want to delete from the list: ")
        
        # Check if input is a valid integer and within range
        if task_index.isdigit():
            task_index = int(task_index)
            if 1 <= task_index <= len(todo_list):
                deleted_task = todo_list.pop(task_index - 1)
                print(f"\n{deleted_task} Task is deleted successfully from your Todo-List")
            else:
                print("\nInvalid index. Please enter a valid task index.")
        else:
            print("\nInvalid input. Please enter a number.")

# Function to update a task in the Todo List
def update_task():
    view_task()
    if todo_list:
        task_index = input("\nEnter the index number of the Task you want to update: ")
        
        # Check if input is a valid integer and within range
        if task_index.isdigit():
            task_index = int(task_index)
            if 1 <= task_index <= len(todo_list):
                new_task_name = input("Now Enter new Task name: ")
                todo_list[task_index - 1] = new_task_name
                print(f"\nTask at index no {task_index} updated successfully [For updated list, check 'View Todo-List']")
            else:
                print("\nInvalid index. Please enter a valid task index.")
        else:
            print("\nInvalid input. Please enter a number.")

if __name__ == "__main__":
    main()
