"""Networking parsing utilities and controller communication."""

import asyncio


def parse_flow_header(raw_data: bytes) -> dict[str, str]:
    """
    Parse a mock network flow header into a dictionary.

    Args:
        raw_data: The raw byte string of the packet.

    Returns:
        A dictionary containing the protocol and status.

    """
    return {"protocol": "TCP", "status": "active" if raw_data else "inactive"}


async def fetch_controller_status() -> str:
    """
    Simulate fetching the status of an asynchronous SDN controller.

    Returns:
        A string representing the system status.

    """
    await asyncio.sleep(0.01)
    return "operational"
