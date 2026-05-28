from datetime import datetime

N_FISIER = "inventar_alimente.txt"


def initializeaza_stoc():
    try:
        f = open(N_FISIER, "r")
        f.close()
    except Exception:
        f = open(N_FISIER, "w")
        f.close()


def adauga_aliment():
    try:
        nume = input("Nume produs: ")
        cantitate = int(input("Cantitate: "))
        data_input = input("Data expirare (ZZ-LL-AAAA): ")

        datetime.strptime(data_input, "%d-%m-%Y")

        f = open(N_FISIER, "a")
        f.write("%s,%d,%s\n" % (nume, cantitate, data_input))
        f.close()
        print("Produs adaugat cu succes!")

    except ValueError:
        print("Eroare")


def afiseaza_raport_si_alerte():
    try:
        f = open(N_FISIER, "r")
    except Exception:
        print("Eroare")
        return

    data_referinta = datetime(2026, 5, 28)

    print("\n--- STARE INVENTAR (Referinta: 28.05.2026) ---")
    print("-" * 75)

    linii = f.readlines()
    f.close()

    if len(linii) == 0:
        print("Inventarul este gol!")
        return

    for linie in linii:
        linie = linie.strip()
        if not linie:
            continue

        componente = linie.split(",")
        nume = componente[0]
        cantitate = componente[1]
        data_str = componente[2]

        try:
            data_exp = datetime.strptime(data_str, "%d-%m-%Y")
            diferenta = (data_exp - data_referinta).days

            if diferenta < 0:
                status = "EXPIRAT"
            elif diferenta <= 3:
                status = "URGENT (%d zile)" % diferenta
            else:
                status = "In termen"

            print("Produs: %s | Cant: %s | Expira: %s | Status: %s" %
                  (nume, cantitate, data_str, status))
        except ValueError:
            continue


def sterge_produs_distribuit():
    nume_cautat = input("Introduceti numele produsului de sters: ")

    try:
        f = open(N_FISIER, "r")
        linii = f.readlines()
        f.close()
    except Exception:
        print("Eroare")
        return

    linii_ramase = []
    gasit = False

    for linie in linii:
        if linie.strip():
            componente = linie.strip().split(",")
            if componente[0] == nume_c;