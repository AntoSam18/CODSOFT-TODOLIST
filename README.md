 # 📝 To-Do List Application (Python + SQLite)

A simple command-line **To-Do List Manager** built with Python, SQLite, and system notifications using `plyer`.  
This app allows you to **add tasks, mark them as completed, view pending tasks, track overdue tasks, and get notifications**.

---

## 🚀 Features
- Add tasks with title, category, due time, and priority
- View tasks sorted by category and due time
- Mark tasks as completed
- Track **pending** and **overdue** tasks with simple metrics
- Get **desktop notifications** for overdue tasks

---

## 📂 Project Structure
```
todo-list-app/
├── antotodo.py              # Main application script
├── database.py          # Database setup and helper functions
├── requirements.txt     # Dependencies
├── todo-videolink.txt   #Detailed Video Explanation
└── README.md            # Documentation
```

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   cd todo-list-app
   ```
   ###2.Install Dependencies
   ```
   pip install -r requirements.txt
   ```
   Usage
   Run the Application
   ```
   python todo.py
   ```
    Example workflow:
   ```
  
   Add new tasks with category, due date, and priority.
   Display all tasks in an organized view.
   Mark tasks as completed when done.
   View pending/overdue metrics.
   Send overdue task reminders as notifications.
   ```
   Dependencies
   ```
   
   sqlite3 (built-in)
   datetime (built-in)
   plyer (for notifications)
   ```
   Install plyer manually if not using requirements.txt:
   ```
   pip install plyer
   ```
   ###Example Output
   ```
   To-Do List Application
   1. Add Task
   2. Display Tasks
   3. Mark Task as Completed
   4. Show Metrics
   5. Send Notifications
   6. Exit

   Your To-Do List:
   ID: 1, Title: Submit Assignment, Category: Professional, Due: 2025-08-20 18:00, Priority: 5,Status: ✘
   ```
   ### Notifications
   When tasks are overdue, desktop notifications are triggered:
   ```
   [Notification]
    Overdue Task Reminder
    Task 'Submit Assignment' is overdue!
   ```
    👨‍💻 Author

    ***Developed by Anto Sam Christ A✨***

   


