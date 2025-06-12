# 📝 To-Do List Application (Python + SQLite + Notifications)

A simple command-line To-Do List manager built in Python. It stores tasks in a SQLite database, supports task categorization and prioritization, and sends notifications for overdue tasks using the `plyer` library.

---

## 📦 Features

- 📋 Add tasks with title, category, due time, and priority
- ✅ Mark tasks as completed
- 📊 View all tasks sorted by category and due time
- 📈 Get metrics for pending and overdue tasks
- 🔔 System notifications for overdue tasks (using `plyer`)
- 🗂️ Categories supported: Personal and Professional
- 🧠 Priority scale: 1 (Low) to 5 (High)

---

## 💾 Requirements

- Python 3.x
- `plyer` (for sending desktop notifications)

Install dependencies using pip:

```bash
'pip install plyer'
