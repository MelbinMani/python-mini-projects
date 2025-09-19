tasks = []


def add_tasks(tasks):
    new_tasks = [x.strip() for x in input(
        "Enter the task(s) to be added (separated by commas):\n").split(",") if x.strip()]
    tasks.extend(new_tasks)
    for i, task in enumerate(new_tasks, 1):
        print(f"✅ {i} : '{task}' added!")


def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def remove_task(tasks):
    try:
        indices = sorted(set([
            int(x.strip()) for x in input("Enter task numbers to remove (comma-separated):\n").split(",")
            if x.strip().isdigit()
        ]), reverse=True)

        for x in indices:
            if 1 <= x <= len(tasks):
                removed = tasks.pop(x - 1)
                print(f"❌ Removed task {x}: '{removed}'")
            else:
                print(f"⚠️ Invalid task number: {x}")
    except Exception as e:
        print(f"⚠️ Error: {e}")


def clear_tasks(tasks):
    tasks.clear()
    print("🗑️ All tasks cleared!")


while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Clear all tasks")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ").strip()

    if choice == "1":
        add_tasks(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        clear_tasks(tasks)
    elif choice == "5":
        print("👋 Exiting To-Do List. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
