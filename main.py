import os
pad_map = "C:/Users/lyamb/Desktop/Deltion_Informatie"
os.listdir()
import os


def hernoem_en_nummer_bestanden(map_naam):
    if not os.path.isdir(map_naam):
        print(f"De map '{map_naam}' bestaat niet.")
        return

    bestanden = os.listdir(map_naam)
    afbeelding_extensies = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    afbeeldingen = [bestand for bestand in bestanden if os.path.splitext(bestand)[1].lower() in afbeelding_extensies]
    afbeeldingen.sort()

    originele_namen_pad = os.path.join(map_naam, "originele_bestandsnamen.txt")

    with open(originele_namen_pad, "w") as f:
        for index, originele_naam in enumerate(afbeeldingen, start=1):
            _, extensie = os.path.splitext(originele_naam)
            nieuwe_naam = f"movie_poster_{index:02d}{extensie.lower()}"
            oud_pad = os.path.join(map_naam, originele_naam)
            nieuw_pad = os.path.join(map_naam, nieuwe_naam)

            os.rename(oud_pad, nieuw_pad)
            f.write(f"{nieuwe_naam}|{originele_naam}\n")

    print(f"{len(afbeeldingen)} bestanden hernoemd en originele namen opgeslagen in 'originele_bestandsnamen.txt'")


def herstel_naar_originele_namen(map_naam):
    originele_namen_pad = os.path.join(map_naam, "originele_bestandsnamen.txt")

    if not os.path.exists(originele_namen_pad):
        print("Geen bestand met originele namen gevonden.")
        return

    met_open_fout = False
    with open(originele_namen_pad, "r") as f:
        for regel in f:
            try:
                nieuwe_naam, originele_naam = regel.strip().split("|")
                oud_pad = os.path.join(map_naam, nieuwe_naam)
                nieuw_pad = os.path.join(map_naam, originele_naam)
                os.rename(oud_pad, nieuw_pad)
            except Exception as e:
                print(f"Fout bij hernoemen: {e}")
                met_open_fout = True

    if not met_open_fout:
        print("Alle bestanden succesvol teruggezet naar hun originele naam.")
    else:
        print("Sommige bestanden konden niet worden teruggezet.")


def main():
    print("1. Hernoem en nummer bestanden")
    print("2. Hernoem bestanden naar originele naam")
    keuze = input("keuze ? ")

    if keuze == "1":
        map_naam = input("Geef de naam van de map met afbeeldingen: ")
        hernoem_en_nummer_bestanden(map_naam)
    elif keuze == "2":
        map_naam = input("Geef de naam van de map waarin 'originele_bestandsnamen.txt' staat: ")
        herstel_naar_originele_namen(map_naam)
    else:
        print("Ongeldige keuze.")


if __name__ == "__main__":
    main()
