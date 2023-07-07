import json

def read_tasks():
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    return tasks

def write_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

def list_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"{i + 1}: {task['task']} on {task['date']} at {task['time']}")

def remove_task(task_number, tasks):
    if task_number > len(tasks) or task_number < 1:
        print("Invalid task number. No task removed.")
        return tasks
    else:
        del tasks[task_number - 1]
        print("Task removed.")
        return tasks

if __name__ == "__main__":
    tasks = read_tasks()
    while True:
        list_tasks(tasks)
        print("Type 'remove <number>' to remove a task or 'quit' to exit.")
        command = input("> ")
        if command.lower() == 'quit':
            break
        elif 'remove' in command.lower():
            task_number = int(command.split()[1])
            tasks = remove_task(task_number, tasks)
            write_tasks(tasks)
