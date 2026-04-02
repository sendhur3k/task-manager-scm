tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def view_tasks():
    for i, t in enumerate(tasks):
        print(i+1, t)

while True:
    print("\n1.Add Task  2.View Tasks  3.Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        task = input("Enter task: ")
        add_task(task)
    elif ch == '2':
        view_tasks()
    elif ch == '3':
        break
