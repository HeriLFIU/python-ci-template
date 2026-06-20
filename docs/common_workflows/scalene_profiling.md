# ⏱️ Scalene Profiling

We use [Scalene](https://github.com/plasma-umass/scalene) for high-resolution profiling of CPU, memory, and copying behavior. Scalene helps identify bottlenecks and memory leaks at the line level, including separating Python vs. native (C) time.

## Day-to-Day Workflows

### 1. Live Interactive Profiling (Local Web UI)

To profile the main application and view results in a live dashboard, run our provided command (e.g. via `make profile`). Under the hood, this typically does:

```bash
uv run scalene run src/my_project/main.py
```

Scalene will open a local web UI showing CPU and memory profiles updated in real time (often at `localhost:5000`). The profiler sampling overhead is low, so you can interact with the program normally and watch bottlenecks and hotspots appear in the browser.

### 2. Generating Standalone HTML Reports

For sharing or offline analysis, generate a self-contained HTML report. Our wrapper might be `make profile-export`, which does something like:

```bash
uv run scalene run --json report.json src/my_project/main.py
uv run scalene view --json report.json --html --standalone
```

This produces a standalone HTML file (e.g. in a `.reports/` directory) that contains interactive graphs of CPU, memory, and copy profiles. (Scalene’s `--standalone` mode embeds all assets into one HTML for easy sharing.)

### 3. Profiling Specific Scripts or Tests

You can profile any Python file or test by invoking Scalene directly. For example, to profile a utility script:

```bash
uv run scalene run src/my_project/utils/special_tool.py
```

To profile a specific test case, run pytest under Scalene:

```bash
uv run scalene run -m pytest tests/test_specific_feature.py
```

This will generate a profile (saved to `scalene-profile.json` by default) for that run. You can then use `scalene view` to examine it. For example:

```bash
# Profile a test
uv run scalene run -m pytest tests/test_specific_feature.py

# View the profile in HTML
uv run scalene view --html --standalone scalene-profile.json
```

These commands follow Scalene’s usage patterns to capture and inspect performance data.
