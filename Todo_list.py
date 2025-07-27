import tkinter as tk
from tkinter import messagebox

# Main app window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

tasks = []

# Function to update listbox
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete selected task
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task = tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# UI Components
title = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=25)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#4caf50", fg="white")
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Selected Task", command=delete_task, font=("Helvetica", 12), bg="#f44336", fg="white")
delete_btn.pack(pady=5)

task_frame = tk.Frame(root)
task_frame.pack(pady=10)

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(task_frame, height=15, width=40, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
task_listbox.pack()

scrollbar.config(command=task_listbox.yview)

# Run the app
root.mainloop()