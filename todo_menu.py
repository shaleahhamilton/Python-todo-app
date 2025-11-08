tasks = []

while True:
    print("\nWhat do you want to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")

    choice = input("Choose (1/2/3): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        print("\nYour tasks:")
        for t in tasks:
            print("-", t)

    elif choice == "3":
        print("Goodbye! 👋🏾")
        break

    else:
        print("Invalid choice. Try again.")