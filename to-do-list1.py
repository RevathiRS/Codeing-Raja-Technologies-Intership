import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and configure the entry widget
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create and configure the "Add Task" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=10, pady=10)

# Create and configure the listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

# Create and configure the "Delete Task" button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=1, column=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
