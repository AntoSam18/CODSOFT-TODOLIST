# todo.py
from datetime import datetime
from plyer import notification
from database import (
    add_task,
    mark_task_completed,
    fetch_all_tasks,
    fetch_pending_count,
    fetch_overdue_count,
    fetch_overdue_tasks,
    close_connection
)


# ------------------------------
# Display Functions
# ------------------------------
def display_tasks():
    """Display all tasks from the database."""
    tasks = fetch_all_tasks()
    if tasks:
        print("\nYour To-Do List:")
        for task in tasks:
            status = "✔" if task[5] else "✘"
            print(f"ID: {task[0]}, Title: {task[1]}, Category: {task[2]}, "
                  f"Due: {task[3]}, Priority: {task[4]}, Status: {status}")
    else:
        print("\nNo tasks available.")


def show_metrics():
    """Show task metrics: pending and overdue counts."""
    pending = fetch_pending_count()
    overdue = fetch_overdue_count()
    print(f"\nMetrics: Pending Tasks: {pending}, Overdue Tasks: {overdue}")


def send_notifications():
    """Send desktop notifications for overdue tasks."""
    overdue_tasks = fetch_overdue_tasks()
    for task in overdue_tasks:
        notification.notify(
            title="Overdue Task Reminder",
            message=f"Task '{task[0]}' is overdue!",
            timeout=5
        )


# ------------------------------
# Main Menu
# ------------------------------
def main_menu():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Show Metrics")
        print("5. Send Notifications")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Task Title: ")
            category = input("Category (Personal/Professional): ")
            due_time = input("Due Time (YYYY-MM-DD HH:MM): ")
            priority = int(input("Priority (1-5): "))
            add_task(title, category, due_time, priority)

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            task_id = int(input("Enter Task ID to mark as completed: "))
            mark_task_completed(task_id)

        elif choice == "4":
            show_metrics()

        elif choice == "5":
            send_notifications()
            print("Notifications sent!")

        elif choice == "6":
            print("Exiting application. Goodbye!")
            close_connection()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
