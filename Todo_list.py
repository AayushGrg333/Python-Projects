# ========================= to do list app ===================================


import tkinter as tk 
from tkinter import messagebox


class list_of_task:
    def __init__(self):
        self.tasks = [] 

    def add_task(self, task):
        self.tasks.append(task)

    def show_list(self):
        return self.tasks   

    def delete_task(self,index):
       if 0 <= index < len(self.tasks):
            del self.tasks[index]    
       else:
            print("Invalid index . Task not detected")
    
def print_task(list_of_task):
        tasks = list_of_task.show_list()
        if tasks:
            print(" Task List: ")
            for index,task in enumerate(tasks, start=1):
                print(f" {index}. {task}")
        else:
            print("The task is empty")

def add_task_gui():
    task_text = task_entry.get().strip()
    if task_text:
        task_list.add_task(task_text)
        update_task_list()
    
def delete_task_gui():
    index = task_listbox.curselection()
    if index:
        task_list.delete_task(index[0])
        update_task_list()
    else:
        messagebox.showwarning("warning","please select a task to delete")
        
def update_task_list():
    task_listbox.delete(0, tk.END) #deletes all the items from index 0 to end("tk.END")
    for task in task_list.show_list():
        task_listbox.insert(tk.END ,task)
    

  
task_list = list_of_task()

root = tk.Tk()
root.title("To do list app")

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=50, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task_gui)
add_button.grid(row=0, column=1, padx=10, pady=20)

task_listbox = tk.Listbox(root, width=50)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task_gui)
delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  
root.update()
# to center the window
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (root_width / 2))
y = int((screen_height / 2) - (root_height / 2))

root.geometry(f"{root_width}x{root_height}+{x}+{y-35}")

root.mainloop()
    


    