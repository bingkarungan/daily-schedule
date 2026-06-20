import json
import os
from datetime import datetime

FILE = "schedule.json"

def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE) as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_task(data):
    date = input("Date (YYYY-MM-DD, blank = today): ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    time = input("Time (e.g. 09:00): ").strip()
    task = input("Task description: ").strip()

    if date not in data:
        data[date] = []
    data[date].append({"time": time, "task": task, "done": False})
    data[date].sort(key=lambda x: x["time"])
    save(data)
    print("Task added.")

def view_schedule(data):
    date = input("Date (YYYY-MM-DD, blank = today): ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    tasks = data.get(date, [])
    if not tasks:
        print(f"No tasks for {date}.")
        return

    print(f"\n--- Schedule for {date} ---")
    for i, t in enumerate(tasks):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{i+1}. {status} {t['time']} - {t['task']}")
    print()

def mark_done(data):
    date = input("Date (YYYY-MM-DD, blank = today): ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    tasks = data.get(date, [])
    if not tasks:
        print("No tasks found.")
        return

    view_schedule(data)
    try:
        num = int(input("Mark task number as done: ")) - 1
        data[date][num]["done"] = True
        save(data)
        print("Marked as done.")
    except (IndexError, ValueError):
        print("Invalid number.")

def delete_task(data):
    date = input("Date (YYYY-MM-DD, blank = today): ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    tasks = data.get(date, [])
    if not tasks:
        print("No tasks found.")
        return

    view_schedule(data)
    try:
        num = int(input("Delete task number: ")) - 1
        removed = data[date].pop(num)
        save(data)
        print(f"Deleted: {removed['task']}")
    except (IndexError, ValueError):
        print("Invalid number.")

def main():
    print("=== Daily Schedule Maintainer ===")
    data = load()

    while True:
        print("\n1. View schedule")
        print("2. Add task")
        print("3. Mark task done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nChoice: ").strip()
        if choice == "1":
            view_schedule(data)
        elif choice == "2":
            add_task(data)
        elif choice == "3":
            mark_done(data)
        elif choice == "4":
            delete_task(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
