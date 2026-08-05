tasks = []

print("📋 CLI To-Do List Manager")

while True:
    print("\n--- MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if not tasks:
            print("Your list is currently empty!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")

    elif choice == "2":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print(f"Added: '{new_task}'")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove!")
            continue

        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: '{removed}'")
        else:
            print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")