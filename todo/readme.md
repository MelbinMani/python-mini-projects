# 📝 CLI To-Do List Manager

A lightweight command-line utility to manage your daily tasks. Add, view, remove, and clear tasks—all from your terminal. Built with clean logic and emoji feedback for a smooth experience.

---

## 🚀 Features

- ✅ Add multiple tasks at once
- 📋 View all current tasks
- ❌ Remove tasks by number
- 🗑️ Clear all tasks
- 👋 Exit the program gracefully

---

## 🛠️ How It Works

This script runs in a loop, presenting a menu of options. Users interact via numbered choices and comma-separated inputs.

### Menu Options
- Add task
- View tasks
- Remove task
- Clear all tasks
- Exit


### Task Operations

- **Add Tasks**: Input comma-separated task names. Whitespace is trimmed.
- **View Tasks**: Displays all tasks with index numbers.
- **Remove Tasks**: Input comma-separated task numbers to delete. Invalid indices are flagged.
- **Clear Tasks**: Deletes all tasks instantly.
- **Exit**: Ends the program.

---

## ▶️ Usage

Run the script in your terminal:

```bash
python todo.py
```
---
## 📁 File Structure

todo.py       # Main script  
README.md     # Documentation

---

## 📌 Example Interaction

--- To-Do List ---
1. Add task
2. View tasks
3. Remove task
4. Clear all tasks
5. Exit
Enter your choice (1–5): 1
Enter the task(s) to be added (separated by commas):
Buy groceries, Finish report
✅ 1 : 'Buy groceries' added!
✅ 2 : 'Finish report' added!