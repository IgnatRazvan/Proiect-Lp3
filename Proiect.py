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


def afiseaza_lista_alimente():
    try:
        f = open(N_FISIER, "r")
    except Exception:
        print("Eroare")
        return

    print("\n--- LISTA TOATE ALIMENTELE ---")
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

        print("Produs: %s | Cant: %s | Expira: %s" % (nume, cantitate, data_str))


def afiseaza_alerte():
    try:
        f = open(N_FISIER, "r")
    except Exception:
        print("Eroare")
        return

    data_referinta = datetime(2026, 5, 28)

    print("\n--- ALERTE SI TIMP RAMAS PANA LA EXPIRARE ---")

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
            elif diferenta == 0:
                status = "EXPIRA ASTAZI"
            else:
                status = "Mai sunt %d zile" % diferenta

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
            if componente[0] == nume_cautat:
                gasit = True
            else:
                linii_ramase.append(linie)

    f = open(N_FISIER, "w")
    f.writelines(linii_ramase)
    f.close()

    if gasit:
        print("Produsul %s a fost eliminat." % nume_cautat)
    else:
        print("Eroare")


def meniu_principal():
    initializeaza_stoc()

    while True:
        print("\n=== SISTEM GESTIUNE RISIPA ALIMENTARA ===")
        print("1. Adauga produs")
        print("2. Lista alimente")
        print("3. Vezi alerte")
        print("4. Sterge produs")
        print("5. Iesire")

        optiune = input("Alege optiunea: ")

        if optiune == "1":
            adauga_aliment()
        elif optiune == "2":
            afiseaza_lista_alimente()
        elif optiune == "3":
            afiseaza_alerte()
        elif optiune == "4":
            sterge_produs_distribuit()
        elif optiune == "5":
            print("Aplicatia s-a inchis.")
            break
        else:
            print("Eroare")


if __name__ == "__main__":
    meniu_principal()