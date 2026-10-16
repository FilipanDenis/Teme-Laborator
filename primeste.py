import socket
import sys


if len(sys.argv) != 2:
    sys.exit("Utilizare: python3 primeste.py fisier_primit")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 7001))
    server.listen(1)
    print("Astept un fisier de la proxy pe portul 7001...")

    conexiune, adresa = server.accept()
    with conexiune, open(sys.argv[1], "wb") as fisier:
        while True:
            date = conexiune.recv(4096)
            if not date:
                break
            fisier.write(date)

print(f"Fisier salvat: {sys.argv[1]}")
