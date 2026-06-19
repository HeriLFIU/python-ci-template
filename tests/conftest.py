"""Global pytest fixtures and environment setup."""

import pytest


@pytest.fixture(autouse=True)
def _setup_test_environment() -> None:  # pyright: ignore[reportUnusedFunction]
    """Configure the base hermetic testing environment."""
    # Place any global database resets or mock initializations here
    return
