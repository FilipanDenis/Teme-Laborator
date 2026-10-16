import socket
import sys


if len(sys.argv) not in (2, 3):
    sys.exit("Utilizare: python3 trimite.py fisier [ip_proxy]")

ip_proxy = sys.argv[2] if len(sys.argv) == 3 else "127.0.0.1"

with open(sys.argv[1], "rb") as fisier:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip_proxy, 7000))
        while True:
            date = fisier.read(4096)
            if not date:
                break
            client.sendall(date)

print(f"Fisier trimis catre proxy: {sys.argv[1]}")
