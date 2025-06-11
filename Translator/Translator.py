import os
from deep_translator import GoogleTranslator

CHUNK_GROOTTE = 500  # max aantal tekens per vertaal-verzoek

def vertaal_bestand(input_pad, output_pad, source_lang="auto", target_lang="nl"):
    with open(input_pad, "r", encoding="utf-8") as infile:
        tekst = infile.read()

    chunks = [tekst[i:i + CHUNK_GROOTTE] for i in range(0, len(tekst), CHUNK_GROOTTE)]
    vertaalde_chunks = []

    print(f"📄 Vertalen van: {os.path.basename(input_pad)} ({len(chunks)} stukken)")

    for i, chunk in enumerate(chunks):
        try:
            vertaalde = GoogleTranslator(source=source_lang, target=target_lang).translate(chunk)
            vertaalde_chunks.append(vertaalde)
        except Exception as e:
            print(f"⚠️ Fout bij vertaling van stuk {i+1}: {e}")
            vertaalde_chunks.append("[VERTALING MISLUKT]")

    volledige_tekst = "\n".join(vertaalde_chunks)

    try:
        with open(output_pad, "w", encoding="utf-8") as outfile:
            outfile.write(volledige_tekst)
        print(f"✅ Opgeslagen als: {output_pad}\n")
    except Exception as e:
        print(f"❌ Kon bestand niet opslaan: {e}")


def vertaal_map(source_map, target_map, source_lang="auto", target_lang="nl"):
    os.makedirs(target_map, exist_ok=True)

    bestanden = [f for f in os.listdir(source_map) if f.endswith(".txt")]
    if not bestanden:
        print("❌ Geen .txt-bestanden gevonden in de opgegeven map.")
        return

    for bestand in bestanden:
        input_pad = os.path.join(source_map, bestand)
        output_pad = os.path.join(target_map, bestand)
        vertaal_bestand(input_pad, output_pad, source_lang, target_lang)

    print("🎉 Alles is vertaald!")


def main():
    bronmap = input("Geef het pad naar de map met tekstbestanden: ").strip()
    if not os.path.isdir(bronmap):
        print("❌ De opgegeven map bestaat niet.")
        return

    doeltaal = input("Voer de doeltaal in (bijv. 'en', 'nl', 'de'): ").strip()
    doelmap = os.path.join(bronmap, f"vertaald_{doeltaal}")

    vertaal_map(bronmap, doelmap, target_lang=doeltaal)


if __name__ == "__main__":
    main()
