import sys

from task_tracker.task_manager import *


def user_input():
    user_command = sys.argv[1:]

    match user_command:
        case []:
            print("No command provided.")
            return 2
        case ["add", description]:
            add_task(description)
        case ["update", task_id, description]:
            try:
                task_id = int(task_id)
            except ValueError:
                print("Task ID must be an integer.")
                return 2
            return update_task(task_id, description)
        case ["delete", task_id]:
            try:
                task_id = int(task_id)
            except ValueError:
                print("Task ID must be an integer.")
                return 2
            return delete_task(task_id)
        case ["list"]:
            list_all_tasks()
        case ["list", "done"]:
            list_all_tasks_by_status(TaskStatus.DONE)
        case ["list", "todo"]:
            list_all_tasks_by_status(TaskStatus.TODO)
        case ["list", "in-progress"]:
            list_all_tasks_by_status(TaskStatus.IN_PROGRESS)
        case ["list", "not_done"]:
            list_all_not_done_tasks()
        case ["mark-in-progress", task_id]:
            try:
                task_id = int(task_id)
            except ValueError:
                print("Task ID must be an integer.")
                return 2
            return mark_task_in_progress(task_id)
        case ["mark-done", task_id]:
            try:
                task_id = int(task_id)
            except ValueError:
                print("Task ID must be an integer.")
                return 2
            return mark_task_done(task_id)
        case _:
            print("Unknown command or invalid input.")
            return 2
    return 0
