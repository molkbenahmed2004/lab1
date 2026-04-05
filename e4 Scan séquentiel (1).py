def scan_ports(host, ports):
    open_ports = []

    for p in ports:
        if tcp_connect(host, p):
            open_ports.append(p)

    return open_ports