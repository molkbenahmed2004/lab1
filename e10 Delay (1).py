import time

def scan_ports(host, ports, delay=0.05):
    open_ports = []

    for p in ports:
        if tcp_connect(host, p):
            open_ports.append(p)
        time.sleep(delay)

    return open_ports