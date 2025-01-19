# 1: Zufallsgenerator

import random
random.seed()

# 2: Anzahl Aufgaben

anzahl = 0
while anzahl < 1 or anzahl > 10:
    try:
        print("Wie veile Aufgaben (1 bis 10):")
        anzahl = int(input())
    except:
        continue
# 3: Anzahl richtige Ergebnisse
richtig = 0

# 4: Schleife mit gewunschter Anzahl an Aufgaben
for aufgabe in range(1, anzahl + 1):

# 5: Operatorauswahl
    opzahl = random.randint(1, 4)

# 6: operandenauswahl
    if opzahl == 1:
        a = random.randint(-10 , 30)
        b = random.randint(-10, 30)
        op = "+"
        c = a + b
    elif opzahl == 2:
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        op = "-"
        c = a - b
    elif opzahl == 3:
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        op = "*"
        c = a * b

# 7: Sonderfall Division
    elif opzahl == 4:
        c = random.randint(1, 30)
        b = random.randint(1, 30)
        op = "/"
        a = c * b

# 8: Aufgabenstellung
    print(f"Aufgabe {aufgabe} von {anzahl}: {a} {op} {b}")

# 9: Schleife mit 3 Versuchen
    for versuch in range(1, 4):
        # 10: Eingabe
        try:
            print("Bitte Losungsvorschlag eingeben:")
            zahl = int(input())
        except:
            # Umwandlung war nicht erfolgreich
            print("Sie haven keine ganze Zahl eingegeben")
            # Schleife unmittelgar fortsetzen
            continue
        # 11: Kommentar
        if zahl ==c:
            print(zahl, "ist richtig")
            richtig = richtig + 1
            break
        else:
            print(zahl, "ist falsch")

    # 12: Richtiges Ergebnis der Aufgabe
    print("Ergebnis:", c)

# 13: Anzahl richtige Ergebnisse
print(f"Richtig: {richtig} von {anzahl}")