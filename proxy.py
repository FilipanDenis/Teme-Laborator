import socket
import sys


if len(sys.argv) > 2:
    sys.exit("Utilizare: python3 proxy.py [ip_destinatie]")

ip_destinatie = sys.argv[1] if len(sys.argv) == 2 else "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 7000))
    server.listen(1)
    print("Proxy-ul asteapta pe portul 7000...")

    conexiune, adresa = server.accept()
    with conexiune:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as destinatie:
            destinatie.connect((ip_destinatie, 7001))
            while True:
                date = conexiune.recv(4096)
                if not date:
                    break
                destinatie.sendall(date)

print("Fisier retransmis catre destinatie.")
