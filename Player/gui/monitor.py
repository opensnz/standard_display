import screeninfo


def get_primary_monitor() -> screeninfo.Monitor:
    monitors = screeninfo.get_monitors()
    for monitor in monitors:
        if monitor.is_primary == True:
            return monitor
    return screeninfo.Monitor(0,0,0,0)