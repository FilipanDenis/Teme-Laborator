# Teme de lucru - socket-uri

Trei exercitii in Python 3, folosind TCP si biblioteca `socket`.
Nu trebuie instalate biblioteci suplimentare.

In fiecare terminal intra mai intai in folderul exercitiului.
Fiecare program face un singur transfer, apoi se inchide.

## 1. Mesaj intr-un inel de 3 procese

Folder: `ex1_inel`

Mesajul circula astfel: P1 → P2 → P3 → P1.
Acelasi fisier este pornit de trei ori, in procese separate.
Fiecare proces asculta pe propriul port: 5001, 5002 sau 5003.

Porneste programele in aceasta ordine, in trei terminale:

Terminalul 1:

```bash
python3 inel.py 3
```

Terminalul 2:

```bash
python3 inel.py 2
```

Terminalul 3:

```bash
python3 inel.py 1 "Salut!"
```

La final, P1 afiseaza: `P1 a primit inapoi de la P3: Salut!`.

## 2. Transfer de fisier intre doua procese

Folder: `ex2_transfer`

Porneste mai intai receptorul, in primul terminal:

```bash
python3 primeste.py primit.txt
```

In al doilea terminal porneste expeditorul:

```bash
python3 trimite.py fisier.txt
```

Fisierul `fisier.txt` ajunge in `primit.txt`. Conexiunea foloseste portul 6000.
Pentru alt calculator, adauga IP-ul receptorului dupa numele fisierului:

```bash
python3 trimite.py fisier.txt 192.168.1.30
```

## 3. Transfer de fisier prin proxy

Folder: `ex3_proxy`

Datele circula astfel: expeditor → proxy → receptor.
Proxy-ul primeste pe portul 7000 si retransmite spre portul 7001.
Nu salveaza fisierul pe disc.

Test pe acelasi calculator, in trei terminale, in aceasta ordine:

Terminalul 1:

```bash
python3 primeste.py primit.txt
```

Terminalul 2:

```bash
python3 proxy.py
```

Terminalul 3:

```bash
python3 trimite.py fisier.txt
```

Pentru trei calculatoare din aceeasi retea, de exemplu:

| Calculator | Comanda |
| --- | --- |
| Receptor, IP 192.168.1.30 | `python3 primeste.py primit.txt` |
| Proxy, IP 192.168.1.20 | `python3 proxy.py 192.168.1.30` |
| Expeditor, IP 192.168.1.10 | `python3 trimite.py fisier.txt 192.168.1.20` |

Inlocuieste IP-urile din exemplu cu adresele reale si pastreaza ordinea de pornire.
Portul 7001 trebuie sa fie accesibil pe receptor, iar 7000 pe proxy.
La exercitiul 2, portul receptorului este 6000.

## Verificare

Dupa transfer, pe acelasi calculator, poti compara fisierele pe Fedora:

```bash
cmp fisier.txt primit.txt
```

Daca nu afiseaza nimic si se termina fara eroare, fisierele sunt identice.
Se pot transfera si fisiere binare, nu doar text.
Fisierul de iesire este suprascris daca exista; alege un nume diferit de sursa.

Datele sunt citite in bucati de pana la 4096 de octeti, pana la inchiderea conexiunii.
Pentru alt transfer, porneste din nou programele in aceeasi ordine.
Daca apare `Connection refused`, verifica IP-ul si daca receptorul sau proxy-ul este pornit.
Un program care asteapta poate fi oprit cu `Ctrl+C`.

Documentatie: [socket - Python](https://docs.python.org/3/library/socket.html).
