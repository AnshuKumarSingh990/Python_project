import tkinter as tk
from tkinter import messagebox

class TodoListGUI:
    def __init__(self, master):
        self.master = master
        self.tasks = []
        self.task_number = 0

        self.task_list = tk.Listbox(master, width=40)
        self.task_list.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.pack(padx=10, pady=10)

        self.done_button = tk.Button(master, text="Mark as Done", command=self.mark_done)
        self.done_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append({"task": task, "done": False})
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.task_number += 1
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def update_task(self):
        try:
            task_number = self.task_list.curselection()[0]
            task = self.task_entry.get()
            if task != "":
                self.tasks[task_number]["task"] = task
                self.task_list.delete(task_number)
                self.task_list.insert(task_number, task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty")
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to update")

    def mark_done(self):
        try:
            task_number = self.task_list.curselection()[0]
            self.tasks[task_number]["done"] = True
            self.task_list.itemconfig(task_number, fg="green")
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to mark as done")

    def delete_task(self):
        try:
            task_number = self.task_list.curselection()[0]
            del self.tasks[task_number]
            self.task_list.delete(task_number)
            self.task_number -= 1
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete")


def main():
    root = tk.Tk()
    root.title("To-Do List")
    todo = TodoListGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
