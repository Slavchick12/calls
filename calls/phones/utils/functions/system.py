"""System info functions."""

import socket


def get_local_ip() -> str:
    """Get IP local machine.

    Returns:
        IP local machine
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('8.8.8.8', 80))
    local_ip = sock.getsockname()[0]
    sock.close()
    return local_ip
