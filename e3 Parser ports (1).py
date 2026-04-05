def parse_ports(s: str) -> list[int]:
    ports = set()

    for part in s.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))

    return sorted(ports)