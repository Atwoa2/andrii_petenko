import time

tasks = []

def show_menu():
    print("\n==== TO-DO MENU ====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Work on task (start timer)")
    print("4. Mark task as done")
    print("5. Remove task")
    print("6. Exit")

def add_task():
    task_name = input("Enter task: ")
    task = {"name": task_name, "done": False, "time_spent": 0}
    tasks.append(task)
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            minutes = task["time_spent"] // 60
            seconds = task["time_spent"] % 60
            print(f"{idx}. {task['name']} [{status}] - Time spent: {minutes}m {seconds}s")

def work_on_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to work on: ")) - 1
            if 0 <= index < len(tasks):
                print(f"⏱️ Working on: {tasks[index]['name']} (press ENTER to stop)")
                start = time.time()
                input()
                end = time.time()
                elapsed = int(end - start)
                tasks[index]["time_spent"] += elapsed
                print(f"⏳ Time recorded: {elapsed} seconds")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_task_done():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                print(f"✅ Marked as done: {tasks[index]['name']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"🗑️ Removed: {removed['name']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        work_on_task()
    elif choice == '4':
        mark_task_done()
    elif choice == '5':
        remove_task()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
