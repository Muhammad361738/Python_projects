import click # for creating cli

import json # to save and load the task froom files
import os # to check if the files exist 

TODO_FILE = "todo.json"

def load_task():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE,"r") as file:
        return json.load(file)

def save_tasks (tasks):
    with open (TODO_FILE,"w") as file :
        json.dump(tasks,file, indent=4)
        
@click.group()
def cli():
    """Simple Todo list manager """
    pass


@click.command()
@click.argument("task")
def add (task):
    """ Add a new task to the list  """
    tasks = load_task()
    tasks.append({"task":task,"done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfuly : {task}")

@click.command()
def list():
    tasks = load_task()
    if not tasks:
        click.echo("No task found")
        return 
    for index , task in enumerate(tasks,1):
        status = "✅" if task ["done"] else "❌"
        click.echo(f"{index}. {task ['task']} [{status}]")  

@click.command()
@click.argument("task_number",type=int)
def complete(task_number):
    """Mark a task as complete """
    tasks = load_task()
    if 0 < task_number <- len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as complete ")
    else:
        click.echo(f"Invalid task number : {task_number}")
        

@click.command()
@click.argument("task_number",type=int)
def remove(task_number):
    """Remove a task from te list"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        removd_task = tasks.pop(task_number -1 )
        save_tasks(tasks)
        click.echo(f"Removed task : {removd_task["task"]}")
    else: 
        click.echo(f"Invalid task number ")

  
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)
if __name__ == "__main__":
    cli()