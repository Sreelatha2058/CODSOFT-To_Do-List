tasks = []

def display_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    display_tasks()
    if tasks:
        while True:
            try:
                task_num = int(input("Enter the task number to remove: "))
                removed = tasks.pop(task_num - 1)
                print(f"Removed task: {removed}")
                break
            except IndexError:
                print("Invalid task number! Please try again.")
            except ValueError:
                print("Please enter a valid number!")


while True:
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
