# Makefile Shortcuts

## 🛠️ Local Developer Commands

Memorizing commands is very difficult.
Here you have a lot of common workflows/commands made easy and accessible to use.

| Command          | Description                                                     |
| ---------------- | --------------------------------------------------------------- |
| `make setup`     | Hydrates the uv environment and installs git hooks.             |
| `make lint`      | Runs the full suite of prek hooks across all local files.       |
| `make format`    | Performs a lightning-fast auto-format using Ruff.               |
| `make typecheck` | Executes Pyright in isolated strict mode.                       |
| `make test`      | Runs the Pytest suite locally.                                  |
| `make profile`   | Launches the local Scalene profiler and opens the live web GUI. |
| `make lock`      | Resolves dependencies and updates the `uv.lock` file.           |
