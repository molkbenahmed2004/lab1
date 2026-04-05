def grab_banner(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(2.0)
        sock.connect((host, port))

        data = sock.recv(1024)
        sock.close()

        if data:
            return data.decode('utf-8', errors='replace')
        return None

    except Exception:
        return None