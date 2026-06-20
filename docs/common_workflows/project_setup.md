# ⚙️ Project Setup

## Explanation

For minimal CI, linting, formatting, and much more, the .pre-commit-config.yaml file can be copied, and you can run one of two scripts depending on your setup. You can run python-ci-template/scripts/interactive/prek-setup.interactive.sh or python-ci-template/scripts/non-interactive/setup-prek.sh. The interactive one is currently much better. Prek is the Rust rewrite of pre-commit, a tool that can run automated workflows whenever you perform actions with Git. It uses Git hooks; you can also use it with GitHub Actions or whatever other tool is being used to manage CI, like Jenkins. It is very useful, highly portable, and customizable; you can even use PreK in C projects and JavaScript projects.

## How a general setup should look

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo
```

Ensure you are at the root of the repository in the next step.

### Step 2: Run the Setup Wrapper

We have a `Makefile` to bootstrap the project environment. Make sure you have `make` installed, then run:

```bash
make setup
```

This setup step does several things automatically:

- Validates that you’re in the project root (where `pyproject.toml` lives).
- Runs `uv sync` to create and populate the virtual environment `.venv` with the locked dependencies.
- Installs the PreK Git hooks (`prek install`).
- Installs Commitizen hooks (so `cz commit` or `git commit` triggers the wizard).

After `make setup` completes, your environment is fully synchronized and ready for development.
