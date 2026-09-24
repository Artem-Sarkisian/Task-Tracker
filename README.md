# Task Tracker CLI

A small command-line app for tracking tasks in a JSON file. You can add tasks, change their descriptions or status, delete them, and list them by status. It uses only the Python standard library at runtime.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) for the commands below, or `pip` to install the project into a virtual environment

## Run it

From the project directory, set up the uv environment once and then run commands:

```bash
uv sync
uv run task-cli add "Buy groceries"
uv run task-cli list
```

Or use pip in a virtual environment:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
task-cli add "Buy groceries"
```

There is no `requirements.txt` to generate with `pip freeze`: the app has no third-party runtime dependencies. `pyproject.toml` describes the project, and `uv.lock` records uv's resolved versions. A build tool such as `setuptools` may be installed during installation; it is not an application dependency.

To run the root script in PyCharm, set its **Script path** to `main.py` and put a command such as `add "Buy groceries"` in **Parameters**. Without parameters, the program prints `No command provided.` and exits with code `2`.

Each invocation performs one command and exits. Descriptions containing spaces must be quoted in the terminal.

## Commands

| Command | Effect |
| --- | --- |
| `task-cli add "Buy groceries"` | Add a task with status `todo` and print its ID. |
| `task-cli update 1 "Buy groceries and cook dinner"` | Change task 1's description. |
| `task-cli mark-in-progress 1` | Set task 1's status to `in-progress`. |
| `task-cli mark-done 1` | Set task 1's status to `done`. |
| `task-cli delete 1` | Delete task 1. |
| `task-cli list` | List all tasks. |
| `task-cli list todo` | List tasks still to do. |
| `task-cli list in-progress` | List tasks in progress. |
| `task-cli list done` | List completed tasks. |
| `task-cli list not_done` | List tasks that are not done. |

Prefix these examples with `uv run` unless you have installed the project into an activated environment.

For example:

```text
$ uv run task-cli add "Buy groceries"
Task Tracker was started
Task ID: 0 created
$ uv run task-cli list todo
Task Tracker was started
[0] Buy groceries — todo. Created: 2026-09-24T12:00:00, Updated: None
```

An unknown task ID is reported as `Task not found.`. A non-numeric ID produces an error message and exits with code `2`; pass an integer ID from the `add` output.

## Data file

The app creates `tasks.json` in the **current working directory** on first run. It stores a JSON array of tasks. For example:

```json
[
  {
    "id": 0,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-09-24T12:00:00",
    "updatedAt": null
  }
]
```

`createdAt` is set when a task is added; `updatedAt` becomes an ISO-formatted timestamp when its description or status changes. The file is ignored by Git so personal tasks are not committed.
