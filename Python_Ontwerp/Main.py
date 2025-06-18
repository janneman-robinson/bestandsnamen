import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_winst_pie(csv_path, output_dir="grafieken"):
    # Lees het CSV-bestand in
    df = pd.read_csv(csv_path, sep=";")

    # Sorteer op winst en pak de top 5
    top5 = df.sort_values(by="Winst", ascending=False).head(5)

    # Output folder
    os.makedirs(output_dir, exist_ok=True)

    # Waarden en labels
    waarden = top5["Winst"]
    labels = top5["Bedrijfsnaam"]

    # Functie voor het tonen van de winstbedragen in de taart
    def format_winst(pct, allvals):
        absolute = int(pct / 100.0 * sum(allvals))
        return f"{absolute} EUR"

    # Teken de taartgrafiek
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        waarden,
        labels=labels,
        autopct=lambda pct: format_winst(pct, waarden),
        startangle=140,
        textprops=dict(color="black")
    )

    # Zet stijl voor labels buiten de taart
    for text in texts:
        text.set_fontsize(10)
        text.set_color("black")

    # Zet stijl voor tekst in de taart
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color("white")

    plt.title("Top 5 Bedrijven met Hoogste Winst (bedragen in de cirkel)")
    plt.axis("equal")

    # Opslaan
    output_path = os.path.join(output_dir, "top5_winst.png")
    plt.savefig(output_path)
    plt.close()

    print(f"Taartdiagram opgeslagen als: {output_path}")

# Voorbeeld aanroep
if __name__ == "__main__":
    generate_winst_pie("bedrijven.csv")
