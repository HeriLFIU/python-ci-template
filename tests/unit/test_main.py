"""Unit tests for the main application entry point."""

import logging

import pytest
from pytest_mock import MockerFixture

from amlight_programmable_data_plane.main import main


def test_main_execution(mocker: MockerFixture, caplog: pytest.LogCaptureFixture) -> None:
    """Verify that main executes and logs correctly without printing to stdout."""
    caplog.set_level(logging.INFO)

    # Using pytest-mock to spy on the internal logger
    spy = mocker.spy(logging.getLogger("amlight_programmable_data_plane.main"), "info")

    exit_code = main()

    assert exit_code == 0
    assert spy.call_count == 1
    assert "Initializing amlight-programmable-data-plane..." in caplog.text
