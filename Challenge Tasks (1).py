import socket

# Challenge B: Service mapping dictionary
SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-alt"
}

def is_open(host, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

host  = input("Host: ").strip()
start = int(input("Start port: ").strip())
end   = int(input("End port:   ").strip())

open_ports = [] # To store results for Challenge A

print(f"\nScanning {host} ports {start}–{end}...\n")

for port in range(start, end + 1):
    if is_open(host, port):
        # Challenge B: Look up service name, default to "Unknown"
        service = SERVICES.get(port, "Unknown")
        result = f"[+] Port {port} ({service}) is OPEN"
        print(result)
        open_ports.append(result)

# Challenge A: Print total count and save to file
print(f"\n--- Scan Complete ---")
print(f"Total open ports found: {len(open_ports)}")

with open("scan_results.txt", "w") as f:
    f.write(f"Scan Results for {host}\n")
    f.write("\n".join(open_ports))
    f.write(f"\n\nTotal open ports: {len(open_ports)}")
    
print("Results saved to scan_results.txt")