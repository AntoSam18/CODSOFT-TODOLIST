# database.py
import sqlite3

# ------------------------------
# Database Connection & Setup
# ------------------------------
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


# ------------------------------
# Database Helper Functions
# ------------------------------

def add_task(title, category, due_time, priority):
    """Add a new task to the database."""
    cursor.execute(
        'INSERT INTO tasks (title, category, due_time, priority, completed) VALUES (?, ?, ?, ?, ?)',
        (title, category, due_time, priority, False)
    )
    conn.commit()
    print(f"Task '{title}' added successfully!")


def mark_task_completed(task_id: int):
    """Mark a specific task as completed."""
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    print(f"Task ID {task_id} marked as completed!")


def fetch_all_tasks():
    """Fetch all tasks sorted by category and due time."""
    cursor.execute('SELECT * FROM tasks ORDER BY category, due_time')
    return cursor.fetchall()


def fetch_pending_count():
    """Get the number of pending tasks."""
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE completed = 0')
    return cursor.fetchone()[0]


def fetch_overdue_count():
    """Get the number of overdue tasks."""
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE due_time < datetime("now") AND completed = 0')
    return cursor.fetchone()[0]


def fetch_overdue_tasks():
    """Get overdue tasks for notifications."""
    cursor.execute('SELECT title FROM tasks WHERE due_time < datetime("now") AND completed = 0')
    return cursor.fetchall()


def close_connection():
    """Close the database connection."""
    conn.close()
