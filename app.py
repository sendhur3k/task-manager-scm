tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        print("\nTasks List:")
        for i, t in enumerate(tasks):
            print(i+1, t)

import sys

# If running in terminal → allow user input
if sys.stdin.isatty():
    while True:
        print("\n1.Add Task  2.View Tasks  3.Exit")
        ch = input("Enter choice: ")

        if ch == '1':
            task = input("Enter task: ")
            add_task(task)
        elif ch == '2':
            view_tasks()
        elif ch == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

# If running in GitHub Actions → auto demo (no input)
else:
    print("Running in CI/CD mode...\n")
    add_task("Sample Task 1")
    add_task("Sample Task 2")
    view_tasks()
