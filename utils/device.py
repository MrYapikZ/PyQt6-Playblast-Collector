import platform, socket, os

def get_machine_name():
    # Try several sources, strip any ".local" etc.
    name = (platform.node()
            or os.environ.get("COMPUTERNAME")
            or os.environ.get("HOSTNAME")
            or socket.gethostname())
    return (name or "UNKNOWN").split('.')[0]
