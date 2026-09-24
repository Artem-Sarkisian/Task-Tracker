from task_tracker.file_manager import (
    create_task,
    delete_task_file,
    find_tasks_by_status,
    update_task_file,
)
from task_tracker.task_status import TaskStatus


def add_task(description: str, status: TaskStatus = TaskStatus.TODO) -> str:
    id = create_task(description, status)
    print(f"Task ID: {id} created")


def update_task(id: int, description: str):
    if update_task_file(id, description):
        print(f"Task ID: {id} updated")
        return 0
    else:
        print("Task not found.")
        return 1


def delete_task(id: int):
    if delete_task_file(id):
        print(f"Task ID: {id} deleted")
        return 0
    else:
        print("Task not found.")
        return 1


def mark_task_in_progress(id: int):
    if update_task_file(id, status=TaskStatus.IN_PROGRESS):
        print(f"Task ID: {id} updated")
        return 0
    else:
        print("Task not found.")
        return 1


def mark_task_done(id: int):
    if update_task_file(id, status=TaskStatus.DONE):
        print(f"Task ID: {id} updated")
        return 0
    else:
        print("Task not found.")
        return 1


def list_all_tasks():
    tasks = find_tasks_by_status(TaskStatus.TODO)
    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} — {task['status']}. Created: {task['createdAt']}, Updated: {task['updatedAt']}"
        )
        print("–––––––––––––––––––––––––")
    tasks = find_tasks_by_status(TaskStatus.IN_PROGRESS)
    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} — {task['status']}. Created: {task['createdAt']}, Updated: {task['updatedAt']}"
        )
        print("–––––––––––––––––––––––––")
    tasks = find_tasks_by_status(TaskStatus.DONE)
    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} — {task['status']}. Created: {task['createdAt']}, Updated: {task['updatedAt']}"
        )


def list_all_not_done_tasks():
    tasks = find_tasks_by_status(TaskStatus.TODO)
    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} — {task['status']}. Created: {task['createdAt']}, Updated: {task['updatedAt']}"
        )
        print("–––––––––––––––––––––––––")
    tasks = find_tasks_by_status(TaskStatus.IN_PROGRESS)
    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} — {task['status']}. Created: {task['createdAt']}, Updated: {task['updatedAt']}"
        )


def list_all_tasks_by_status(status: TaskStatus):
    tasks = find_tasks_by_status(status)
    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} — {task['status']}. Created: {task['createdAt']}, Updated: {task['updatedAt']}"
        )
