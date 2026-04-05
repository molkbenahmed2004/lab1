COMMON = {
    22: 'SSH',
    80: 'HTTP',
    443: 'HTTPS',
    3306: 'MySQL'
}

def guess_service(port, banner):
    return banner if banner else COMMON.get(port, 'inconnu')