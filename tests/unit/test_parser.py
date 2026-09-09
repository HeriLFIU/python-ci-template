"""Unit tests demonstrating advanced pytest plugins."""

import socket
import typing

import pytest
from pytest_benchmark.fixture import BenchmarkFixture
from syrupy.assertion import SnapshotAssertion

from foo.parser import fetch_controller_status, parse_flow_header


def test_parse_flow_header_snapshot(snapshot: SnapshotAssertion) -> None:
    """Demonstrate syrupy snapshot testing for complex dictionary structures."""
    raw_packet = b"\x04\x01\x00\x50"
    result = parse_flow_header(raw_packet)

    # syrupy will automatically generate a __snapshots__ directory to store this state
    assert result == snapshot


def test_parse_flow_header_performance(benchmark: BenchmarkFixture) -> None:
    """Demonstrate pytest-benchmark for critical-path algorithms."""
    raw_packet = b"\x04\x01\x00\x50"

    result = typing.cast("dict[str, str]", benchmark(parse_flow_header, raw_packet))

    assert result["protocol"] == "TCP"


@pytest.mark.asyncio
async def test_fetch_controller_status_async() -> None:
    """Demonstrate pytest-asyncio for testing asynchronous coroutines."""
    status = await fetch_controller_status()
    assert status == "operational"


def _attempt_outbound_connection() -> None:
    """Try to reach a non-loopback address, which pytest-socket must block."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        sock.connect(("10.255.255.1", 80))


def test_network_isolation_is_active() -> None:
    """Demonstrate pytest-socket actively blocking rogue network calls."""
    # POSIX blocks socket creation outright via --disable-socket. Windows allows
    # creation (asyncio needs it) but blocks connect() to anything off loopback,
    # so both platforms raise a RuntimeError subclass, just one step apart.
    with pytest.raises(RuntimeError):
        _attempt_outbound_connection()
