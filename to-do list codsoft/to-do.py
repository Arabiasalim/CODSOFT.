import tkinter as tk


def add_task():
    task = input.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def remove_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)


def update_task():
    selected = listbox.curselection()
    if selected:
        task = input.get()
        if task:
            listbox.delete(selected)
            listbox.insert(selected, task)
            input.delete(0, tk.END)


root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=50, pady=10)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

input = tk.Entry(root, width=40)
input.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=5)

root.mainloop()

scrollbar = tk.Scrollbar(frame, orient=tk)
