"""Unit tests for the main application entry point."""

import logging

import pytest
from pytest_mock import MockerFixture

from foo.main import main


def test_main_execution(mocker: MockerFixture, caplog: pytest.LogCaptureFixture) -> None:
    """Verify that main executes and logs correctly without printing to stdout."""
    caplog.set_level(logging.INFO)

    # Using pytest-mock to spy on the internal logger
    spy = mocker.spy(logging.getLogger("foo.main"), "info")

    exit_code = main()

    assert exit_code == 0
    assert spy.call_count == 1
    assert "Initializing foo..." in caplog.text
