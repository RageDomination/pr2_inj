import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    tasks.append(task)
    listbox.insert(tk.END, task)

def delete_task():
    selected = listbox.curselection()
    for i in reversed(selected):
        listbox.delete(i)

def clear_tasks():
    length = listbox.size()
    for i in range(length // 2):
        listbox.delete(0)

root = tk.Tk()
root.title("My App")

root.geometry("200x150")

entry = tk.Entry(root)
entry.pack()

add_btn = tk.Button(root, text="Confirm", command=add_task)  # змiнено онлайн
add_btn.pack()

delete_btn = tk.Button(root, text="Delete", command=delete_task) # кнопка видалити завдання
delete_btn.pack()

clear_btn = tk.Button(root, text="Clear All", command=clear_tasks) # кнопка стерти все
clear_btn.pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()
