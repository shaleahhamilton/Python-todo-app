tasks = []

while True:
    print("\nWhat do you want to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")

    choice = input("Choose (1/2/3/4): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        print("\nYour tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        print("\nYour tasks:")
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

            num = input("Enter the task number to delete: ")

            if num.isdigit() and 1 <= int(num) <= len(tasks):
                removed = tasks.pop(int(num) - 1)
                print(f"🗑️ Deleted: {removed}")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        print("Goodbye! 👋🏾")
        break

    else:
        print("Invalid choice. Try again.")