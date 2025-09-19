#Task1
#ToDoList
import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete selected task
def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    listbox.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Input field
entry = tk.Entry(root, width=35)
entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", width=15, command=clear_tasks)
clear_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Run the application
root.mainloop()
