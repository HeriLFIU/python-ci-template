# Continuous Python

![CI Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![Tooling](https://img.shields.io/badge/tooling-uv%20%7C%20prek%20%7C%20ruff-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

A repository containing a universal continuous integration template for Python and related projects.

## 📑 Table of Contents

- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Quick Minimal Setup](#-quick-minimal-setup)
- [Usage](#-usage)
- [Additional Documentation](#-additional-documentation)
- [Contributing](#-contributing)
- [License](#-license)

______________________________________________________________________

## 📋 Prerequisites

Before cloning the repository, ensure your local machine has the following foundational tools installed:

- **[Git](https://git-scm.com/)**: For version control.
- **[GNU Make](https://www.gnu.org/software/make/)**: Required to execute the `Makefile` developer API commands.
- **Bash-compatible Shell**: Native on Linux/macOS. Windows users should run this within WSL2 or Git Bash.
- *(Optional but recommended)* **[uv](https://docs.astral.sh/uv/)**: Our setup scripts will utilize `uv` if installed globally, drastically speeding up the initial environment hydration.

## 🚀 Quick Start

You can setup everything in two easy steps.

First clone the repository.

```bash
git clone https://github.com/HeriLFIU/python-ci-template.git
```

Then run the following command and you can get started on your python project.

```bash
make setup
```

## 🛠 Quick Minimal Setup

If you do not want to utilize uv (a Python package and project manager replacement for pip) or you have a project that is not fully Python but want to incorporate some quality checks, you can do so by copying the `.pre-commit-config.yaml` file over to your project and then installing and running pre-commit or prek (the rust rewrite of pre-commit).

If this is difficult for you, you can utilize the `python-ci-template/scripts/interactive/prek-setup.interactive.sh` to help you set up the tools in your project.

Make sure the `prek-setup.interactive.sh` bash script is executable.

```bash
./scripts/interactive/prek-setup.interactive.sh
```

You can also run the commands on your own:

Download pre-commit or prek with your package manager of choice. I will be using pip for this example.

```bash
pip install prek
```

Then install the hooks from the configuration file `.pre-commit-config.yaml`.

```bash
prek install
```

Optional: Update all hooks to latest version.

```bash
prek autoupdate
```

Optional: Run hooks on all files.

```bash
prek run --all-files
```

## 💻 Usage

This template aims to provide an experience which is as hands free as possible.

You can write code as you normally would and the CI Pipeline will verify it and take care of the rest.

When you run `make setup` and then run `git commit` or `git commit -m ""`. It will get overridden and run Commitizen, an interactive CLI tool that helps author your commits following the Conventional Commits specification.

The hooks from PreK / Pre-commit are very important. They will verify all of your staged files. Some of the hooks actually fix the issues, and all that you have to do is just re-add them using `git add foo` and then try to commit again. On the other hand, there are hooks that throw an error, and they do not fix the issue themselves. You have to fix it yourself and then add the file to the staging area (yet again) and try to commit again and see if there are any more issues.

**Note:** Some of the errors that you have to fix are just very strict linter and formatter rules, and you can disable them with the configs if you want.

Some configs were not created by default, so you can create them if you want and modify the rules of some of the static analysis tools.

## ⚡ Enterprise Stack & Features

Here are some of the tools used within the template:

- **Dependency Management & Builds:** **[uv](https://docs.astral.sh/uv/)** - A fast Rust-based replacement for `pip` and `virtualenv`. It is very similar to npm (Node Package Manager). It automatically manages the virtual environment, dependencies, and generates a "lockfile" with the current version of all dependencies used so that there is no difference throughout environments.
- **Static Analysis & Formatting:** **[Ruff](https://docs.astral.sh/ruff/)** (replaces Flake8/Black/isort).
- **[Pyright](https://microsoft.github.io/pyright/)** It enforces strict static typing.
- **Pre-commit Hooks:** **[PreK](https://github.com/j178/prek)** - The Rust port of pre-commit, combined with **Commitizen** to automatically enforce Conventional Commits.
- **Testing Infrastructure:** **[Pytest](https://docs.pytest.org/)** configured with `pytest-xdist` for multi-core parallel execution of tests, `pytest-benchmark` for isolated micro-benchmarking, and `diff-cover` it ensures coverage reports only run on the files being changed within a Pull Request.
- **Profiling:** **[Scalene](https://github.com/plasma-umass/scalene)** - A CPU, GPU, and Memory profiler.
- **Automated Releases:** **[Release Please](https://github.com/googleapis/release-please)** - Google's automated release bot. It checks your commit history and generates semantic version tags and changelogs. Commits must follow the conventional commits specification to work.

## 🏗️ Repository Structure

```text
python-ci-template/
├── .github/
│   └── workflows/           # CI/CD pipeline workflows (ci.yml, release-please.yml)
├── docs/                    # General Documentation
├── scripts/                 # Interactive and non-interactive bash scripts for easy setup
├── src/                     # Main application source code
│   └── foo/
├── tests/                   # Pytest test suite
├── .pre-commit-config.yaml  # PreK hook configurations
├── Makefile                 # Unified Developer CLI API
├── pyproject.toml           # Project metadata, dependencies, and tool settings
└── uv.lock                  # Deterministic dependency lockfile
```

## 📚 Additional Documentation

### Tools

- [Tooling](docs/tooling.md)

### Common Workflows

- [Managing Packages with uv](docs/common_workflows/uv_package_manager.md)
- [Ruff Linting & Formatting](docs/common_workflows/ruff_linting_formatting.md)
- [Pytest Unit Testing & Coverage Reports](docs/common_workflows/pytest_unit_testing.md)
- [Building & Managing Project](docs/common_workflows/building_managing_project.md)
- [Commit Authoring with Commitizen](docs/common_workflows/commit_authoring_commitizen.md)
- [Release Please Automated Releases](docs/common_workflows/release_please.md)
- [Prek Quality Checks](docs/common_workflows/prek_quality_checks.md)
- [Pyright Typechecking](docs/common_workflows/pyright_typechecking.md)
- [Adding new prek hooks](docs/common_workflows/new_prek_hooks.md)
- [Project Setup](docs/common_workflows/project_setup.md)
- [Scalene Profiling](docs/common_workflows/scalene_profiling.md)
- [Makefile Shortcuts](docs/common_workflows/makefile_shortcuts.md)
- [CI Pipeline Lifecycle](docs/common_workflows/ci_lifecycle.md)

### Concepts

- [Conventional Commits](docs/concepts/conventional_commits.md)
- [Semantic Versioning](docs/concepts/semantic_versioning.md)
- [Boy Scout Rule](docs/concepts/boy_scout_rule.md)

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## 📄 License

MIT
