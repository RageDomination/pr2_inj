import tkinter as tk

tasks = []

# функцiя додавання
def add_task():
    task = entry.get()
    tasks.append(task)
    listbox.insert(tk.END, task)

# функцiя видалення
def delete_task():
    selected = listbox.curselection()
    for i in reversed(selected):
        listbox.delete(i)

# функцiя стерти все
def clear_tasks():
    length = listbox.size()
    for i in range(length // 2):
        listbox.delete(0)

root = tk.Tk()
root.title("My App") # назва вiкна

root.geometry("200x150") # розмi стартового вiкна

entry = tk.Entry(root)
entry.pack()

add_btn = tk.Button(root, text="Add Task", command=add_task)  # локально
add_btn.pack()

delete_btn = tk.Button(root, text="Delete", command=delete_task) # кнопка видалити завдання
delete_btn.pack()

clear_btn = tk.Button(root, text="Clear All", command=clear_tasks) # кнопка стерти все
clear_btn.pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()
