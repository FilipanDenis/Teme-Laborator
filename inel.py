import socket
import sys


if len(sys.argv) not in (2, 3) or sys.argv[1] not in ("1", "2", "3"):
    sys.exit('Utilizare: python3 inel.py 1|2|3 ["mesaj"]')

numar = int(sys.argv[1])
urmator = numar % 3 + 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 5000 + numar))
    server.listen(1)
    print(f"P{numar} asculta pe portul {5000 + numar}.")

    if numar == 1:
        mesaj = sys.argv[2] if len(sys.argv) == 3 else "Salut din procesul 1!"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(("127.0.0.1", 5002))
            client.sendall(mesaj.encode("utf-8"))
        print(f"P1 a trimis spre P2: {mesaj}")

    conexiune, adresa = server.accept()
    with conexiune:
        mesaj_primit = b""
        while True:
            date = conexiune.recv(4096)
            if not date:
                break
            mesaj_primit += date

    if numar == 1:
        print(f"P1 a primit inapoi de la P3: {mesaj_primit.decode('utf-8')}")
    else:
        print(f"P{numar} a primit: {mesaj_primit.decode('utf-8')}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(("127.0.0.1", 5000 + urmator))
            client.sendall(mesaj_primit)
        print(f"P{numar} a trimis spre P{urmator}.")
