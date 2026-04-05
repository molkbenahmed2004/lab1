def print_report(results):
    for ip, entries in results.items():
        print(f"\n=== {ip} ===")

        name = reverse_dns(ip)
        if name:
            print(f"Nom: {name}")

        for entry in entries:
            port = entry['port']
            banner = entry.get('banner')

            service = guess_service(port, banner)

            print(f"Port {port} -> {service}")