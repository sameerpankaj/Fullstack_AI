# import os


# #File to store tasks
# FILE_NAME = 'tasks.txt'

# #Load tasks from file
# def load_tasks():
#     tasks = {}
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME, 'r') as file:
#             for line in file:
#                 task_id, title, status = line.strip().split(' | ')
#                 task_id[int(task_id)] = {'title': title, 'status': status}

#     return tasks

# #save tasks to file
# def save_tasks(tasks):
#     with open(FILE_NAME, 'w') as file:
#         for task_id, task in tasks.items():
#             file.write(f'{task_id} | {task['title']} | {task['status']}\n')
                       
# #Add a new task
# def add_task(tasks):
#     title = input('Enter a task title: ')
#     task_id = max(tasks.keys(), default=0) + 1
#     tasks[task_id] = {'title': title, 'status': 'incomplete'}
#     print(f"Task '{title}' added.")

# #View all tasks
# def view_tasks(tasks):
#     if not tasks:
#         print('No tasks available')
#     else:
#         for task_id, task in tasks.items():
#             print(f"[{task_id}] {task['title']} - {task['status']}")

# #Mark the task as complete from incomplete status
# def mark_status_complete(tasks):
#     task_id = int(input('Enter task id to mark as complete: '))
#     if task_id in tasks:
#         tasks[task_id]['status'] = 'complete'
#         print(f"Task '{tasks[task_id]['title']}' marked as complete")
#     else:
#         print('Task ID not found. ')


# #Delete a taks
# def delete_task(tasks):
#     task_id = int(input('Enter task id to to delete: '))
#     if task_id in tasks:
#         deleted_task = tasks.pop(task_id)
#         print(f"Task '{deleted_task['title']}' deleted.")
#     else:
#         print('Task ID not found. ')

# #Main Menu
# def main():
#     tasks = load_tasks()
#     while True:
#         print("\nTask Manager Menu: ")
#         print("\1. Add Task: ")
#         print("\2. View Task: ")
#         print("\3. Mark Task as complete: ")
#         print("\4. Delte Task: ")
#         print("\5. Exit : ")
#         choice = input('Enter your choice')

#         if choice == '1':
#             add_task(tasks)
#         elif choice == '2':
#             view_tasks(tasks)
#         elif choice == '3':
#             mark_status_complete(tasks)
#         elif choice == '4':
#             delete_task(tasks)
#         elif choice == '5':
#             save_tasks(tasks)
#             print('Goodbye')
#             break 
#         else:
#             print('Invalid Choice. Please try again')

# if __name__ == '__main__':
#     main()


import os  # Used to check if file exists and handle file operations

# File name where tasks will be stored
FILE_NAME = 'tasks.txt'


# Load tasks from file into a dictionary
def load_tasks():
    tasks = {}  # Empty dictionary to store tasks in memory

    # Check if the file exists before trying to read it
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            # Read file line by line
            for line in file:
                # Split each line into task_id, title, and status
                task_id, title, status = line.strip().split(' | ')

                # Convert task_id to integer and store task in dictionary
                tasks[int(task_id)] = {
                    'title': title,
                    'status': status
                }

    return tasks  # Return all loaded tasks


# Save tasks from dictionary back into file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        # Loop through all tasks in dictionary
        for task_id, task in tasks.items():
            # Write each task in a structured format
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")


# Add a new task
def add_task(tasks):
    title = input('Enter a task title: ')  # Take task input from user

    # Generate new task ID (max existing ID + 1)
    task_id = max(tasks.keys(), default=0) + 1

    # Add task to dictionary
    tasks[task_id] = {
        'title': title,
        'status': 'incomplete'
    }

    print(f"Task '{title}' added.")


# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print('No tasks available')
    else:
        # Loop through tasks and print each one
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")


# Mark a task as complete
def mark_status_complete(tasks):
    task_id = int(input('Enter task id to mark as complete: '))

    # Check if task exists
    if task_id in tasks:
        tasks[task_id]['status'] = 'complete'  # Update status

        print(f"Task '{tasks[task_id]['title']}' marked as complete")
    else:
        print('Task ID not found.')


# Delete a task
def delete_task(tasks):
    task_id = int(input('Enter task id to delete: '))

    # Check if task exists before deleting
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)  # Remove task from dictionary

        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print('Task ID not found.')


# Main program loop (menu system)
def main():
    tasks = load_tasks()  # Load existing tasks from file

    while True:
        # Display menu options
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        # Get user choice
        choice = input('Enter your choice: ')

        # Call functions based on user input
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_status_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)  # Save before exiting
            print('Goodbye')
            break
        else:
            print('Invalid choice. Please try again.')

# Run the program only if this file is executed directly
if __name__ == '__main__':
    main()

'''

👍 What you just built (important!)

This is a real-world mini project that includes:

File handling (open, read, write)
Dictionaries (task storage)
Functions (modular design)
Loops + menus
Basic CRUD system (Create, Read, Update, Delete)

'''