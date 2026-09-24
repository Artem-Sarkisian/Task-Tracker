import datetime
import json

from task_tracker.task_status import TaskStatus


def ensure_tasks_file():
    try:
        with open("tasks.json", "r"):
            pass
    except FileNotFoundError:
        with open("tasks.json", "x") as json_file:
            json.dump([], json_file)


def find_tasks_by_status(status: TaskStatus) -> list | None:
    with open("tasks.json", "r") as json_file:
        data = json.load(json_file)
        result: list = []
        for task in data:
            if task["status"] == status:
                result.append(task)

        return result


def create_task(description: str, status: TaskStatus) -> int:
    with open("tasks.json", "r") as json_file:
        data = json.load(json_file)
        try:
            new_task_id = data[-1]["id"] + 1
        except Exception:
            new_task_id = 0
        data.append(
            {
                "id": new_task_id,
                "description": description,
                "status": status,
                "createdAt": datetime.datetime.now().isoformat(),
                "updatedAt": None,
            }
        )
        with open("tasks.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
            return new_task_id


def update_task_file(
    id: int, description: str | None = None, status: TaskStatus | None = None
) -> bool:
    if description is not None:
        with open("tasks.json", "r") as json_file:
            data = json.load(json_file)
            for task in data:
                if task["id"] == id:
                    task["description"] = description
                    task["updatedAt"] = datetime.datetime.now().isoformat()
                    with open("tasks.json", "w") as json_file:
                        json.dump(data, json_file, indent=4)
                        return True
            else:
                return False
    if status is not None:
        with open("tasks.json", "r") as json_file:
            data = json.load(json_file)
            for task in data:
                if task["id"] == id:
                    task["status"] = status
                    task["updatedAt"] = datetime.datetime.now().isoformat()
                    with open("tasks.json", "w") as json_file:
                        json.dump(data, json_file, indent=4)
                        return True
            else:
                return False


def delete_task_file(id: int) -> bool:
    with open("tasks.json", "r") as json_file:
        data = json.load(json_file)
        for task in data:
            if task["id"] == id:
                data.remove(task)
                with open("tasks.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
                    return True
        else:
            return False
