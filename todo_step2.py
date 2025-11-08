tasks = []

while True:
    task = input("Enter a task (or type 'done' to stop): ")

    if task.lower() == "done":
        break

    tasks.append(task)

print("\nYour tasks:")
for t in tasks:
    print("-", t)