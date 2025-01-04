import sqlite3
from datetime import datetime
from plyer import notification

 
conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT,
    category TEXT,
    due_time TEXT,
    priority INTEGER,
    completed BOOLEAN
)''')
conn.commit()

 
def add_task(title, category, due_time, priority):
    cursor.execute('INSERT INTO tasks (title, category, due_time, priority, completed) VALUES (?, ?, ?, ?, ?)',
                   (title, category, due_time, priority, False))
    conn.commit()
    print(f"Task '{title}' added successfully!")

 
def mark_task_completed(task_id):
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    print(f"Task ID {task_id} marked as completed!")

 
def display_tasks():
    cursor.execute('SELECT * FROM tasks ORDER BY category, due_time')
    tasks = cursor.fetchall()
    if tasks:
        print("\nYour To-Do List:")
        for task in tasks:
            status = "✔" if task[5] else "✘"
            print(f"ID: {task[0]}, Title: {task[1]}, Category: {task[2]}, Due: {task[3]}, Priority: {task[4]}, Status: {status}")
    else:
        print("\nNo tasks available.")

 
def show_metrics():
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE completed = 0')
    pending = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE due_time < datetime("now") AND completed = 0')
    overdue = cursor.fetchone()[0]
    print(f"\nMetrics: Pending Tasks: {pending}, Overdue Tasks: {overdue}")

 
def send_notifications():
    cursor.execute('SELECT title FROM tasks WHERE due_time < datetime("now") AND completed = 0')
    overdue_tasks = cursor.fetchall()
    for task in overdue_tasks:
        notification.notify(
            title="Overdue Task Reminder",
            message=f"Task '{task[0]}' is overdue!",
            timeout=5
        )
 
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
            conn.close()
            break
        
        else:
            print("Invalid choice. Please try again.")

 
if __name__ == "__main__":
    main_menu()
