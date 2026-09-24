import json

from task_tracker.file_manager import ensure_tasks_file
from task_tracker.gateway import user_input


def main():
    print("Task Tracker was started")
    ensure_tasks_file()

    try:
        return user_input()
    except json.JSONDecodeError:
        print("tasks.json contains invalid JSON.")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
