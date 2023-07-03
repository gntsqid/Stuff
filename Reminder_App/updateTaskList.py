import json
import sys

def add_task(task, date, time):
    # Load the existing tasks
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    
    # Add the new task
    tasks.append({"task": task, "date": date, "time": time})
    
    # Write the tasks back to the file
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

# Check that the correct number of arguments was provided
if len(sys.argv) != 4:
    print("Usage: python3 reminder_app.py <task> <date> <time>")
    sys.exit(1)

task = sys.argv[1]
date = sys.argv[2]
time = sys.argv[3]

add_task(task, date, time)

