import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("📝 TO-DO List")
root.geometry("420x600+400+100")
root.resizable(False, False)
root.config(bg="#f5f7fa")

task_list = []
selected_index = None


def addTask():
    global selected_index
    task = task_entry.get().strip()
    task_entry.delete(0, tk.END)

    if add_button['text'] == "Add":
        if task:
            listbox.insert(tk.END, task)
            task_list.append(task)
            with open("tasklist.txt", 'a') as f:
                f.write(task + "\n")
    else:
        i = selected_index[0]
        task_list[i] = task
        listbox.delete(i)
        listbox.insert(i, task)
        with open("tasklist.txt", 'w') as f:
            for t in task_list:
                f.write(t + "\n")
        add_button.config(text="Add")
        selected_index = None


def deleteTask():
    global task_list
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]
    task_list.remove(task_list[index])
    listbox.delete(index)

    with open("tasklist.txt", 'w') as f:
        for t in task_list:
            f.write(t + "\n")


def updateTask():
    global task_list, selected_index
    selected_index = listbox.curselection()
    if selected_index:
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task_list[selected_index[0]])
        add_button.config(text="Update")


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        with open('tasklist.txt', 'w') as file:
            pass

tk.Label(root, text="🗂️  My To-Do List", font=("Helvetica", 22, "bold"), bg="#f5f7fa", fg="#34495e").pack(pady=20)

entry_frame = tk.Frame(root, bg="#f5f7fa")
entry_frame.pack()

task_entry = tk.Entry(entry_frame, font=("Helvetica", 16), width=26, bd=2, relief=tk.FLAT, highlightthickness=2,
                      highlightbackground="#b2bec3", highlightcolor="#0984e3")
task_entry.pack(padx=10, pady=5)
task_entry.focus()

add_button = tk.Button(root, text="Add", font=("Helvetica", 14, "bold"), width=15, pady=8, bg="#00b894", fg="white",
                       activebackground="#00cec9", bd=0, command=addTask)
add_button.pack(pady=(10, 20))

list_frame = tk.Frame(root, bg="#f5f7fa", bd=2)
list_frame.pack(pady=(10, 0))

listbox = tk.Listbox(list_frame, font=("Helvetica", 13), width=35, height=12, bg="#ecf0f1", fg="#2d3436",
                     selectbackground="#0984e3", selectforeground="white", activestyle="none")
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

btn_row = tk.Frame(root, bg="#f5f7fa")
btn_row.pack(pady=30)

update_button = tk.Button(btn_row, text="✏️ Update", font=("Helvetica", 12, "bold"), bg="#6c5ce7", fg="white",
                          activebackground="#a29bfe", bd=0, width=12, pady=8, command=updateTask)
update_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(btn_row, text="🗑️ Delete", font=("Helvetica", 12, "bold"), bg="#d63031", fg="white",
                          activebackground="#ff7675", bd=0, width=12, pady=8, command=deleteTask)
delete_button.grid(row=0, column=1, padx=10)


openTaskFile()
root.mainloop()
