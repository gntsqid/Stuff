import json

def read_tasks():
    # with open(r'C:\Users\Steven\Desktop\Python\tasks.json', 'r') as f:    # for windows
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    return tasks

def generate_message(tasks):
    message = "Hi! Remember that you have to do:\n"
    for task in tasks:
        message += f"{task['task']} on {task['date']} at {task['time']}\n"
    return message

tasks = read_tasks()
message = generate_message(tasks)
print(message)

