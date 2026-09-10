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

## 📊 Expensive Analysis

These are deliberately excluded from `make lint` and the commit hooks. Run them
when you need evidence, not on every change. See
[Reading CI & Profiler Feedback](ci_feedback.md).

| Command        | Description                                                           |
| -------------- | --------------------------------------------------------------------- |
| `make report`  | Full suite with coverage and JUnit XML, written to `.reports/`.       |
| `make bench`   | Micro-benchmarks only, serial, recorded as `.reports/benchmark.json`. |
| `make analyze` | `report` and `bench` together — the full local evidence pass.         |
