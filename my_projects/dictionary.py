dc = {"Peter":31, "Julia":28, "Werner":35}
print("Dictionary:", dc)
print("Anzahl:", len(dc))
print()

dc_vergleich = {"Peter":31, "Werner":35, "Julia":28}
if dc ==dc_vergleich:
    print("Gleich")

dc["Julia"] = 27
print("Wert ersetzt:", dc)

dc["Moritz"] = 22
print("Element hinzugefugt:", dc)

if "Julia" in dc:
    print(f"Schlussel 'Julia': Wert {dc["Julia"]}")
del dc["Julia"]
if "julia" not in dc:
    print(f"Schlussel 'Julia' nicht enthalten")
print("Element entfernt:", dc)

dc_hinzu = {"Moritz":18, "Karin":29}
dc.update(dc_hinzu)
print("Update:", dc)