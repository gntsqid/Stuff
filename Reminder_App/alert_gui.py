import json
from tkinter import *

# function to add to JSON
def write_json(data, filename='tasks.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def add_task():
    with open('tasks.json') as json_file:
        data = json.load(json_file)

        # python object to be appended
        new_task = {"task": task_entry.get(),
                    "date": date_entry.get(),
                    "time": time_entry.get()}

        # appending data
        data.append(new_task)

    write_json(data)

# GUI Code
window = Tk()
window.title("Reminder Updater")

task_label = Label(window, text="Task")
task_label.grid(column=0, row=0)

date_label = Label(window, text="Date")
date_label.grid(column=0, row=1)

time_label = Label(window, text="Time")
time_label.grid(column=0, row=2)

task_entry = Entry(window, width=20)
task_entry.grid(column=1, row=0)

date_entry = Entry(window, width=20)
date_entry.grid(column=1, row=1)

time_entry = Entry(window, width=20)
time_entry.grid(column=1, row=2)

add_button = Button(window, text="Add Task", command=add_task)
add_button.grid(column=0, row=3)

window.mainloop()

