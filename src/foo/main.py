"""Primary entry point for foo."""

import logging

logger = logging.getLogger(__name__)


def main() -> int:
    """
    Execute the primary entry point for the application.

    Returns:
        int: The system exit code.

    """
    logger.info("Initializing foo...")
    return 0


if __name__ == "__main__":
    main()
