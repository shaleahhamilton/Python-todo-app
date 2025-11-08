import os

tasks = []

# Load tasks if file exists
if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())

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

        # Save to file
        with open("tasks.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")

        print("✅ Task added and saved!")

    elif choice == "2":
        print("\nYour tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

            num = input("Enter task number to delete: ")

            if num.isdigit() and 1 <= int(num) <= len(tasks):
                removed = tasks.pop(int(num) - 1)

                with open("tasks.txt", "w") as file:
                    for t in tasks:
                        file.write(t + "\n")

                print(f"🗑️ Deleted: {removed} and saved changes!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        print("Goodbye! 👋🏾")
        break

    else:
        print("Invalid choice. Try again.")