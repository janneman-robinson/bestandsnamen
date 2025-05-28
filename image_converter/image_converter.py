import os
from PIL import Image

def is_image_file(filename):
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    return filename.lower().endswith(image_extensions)

def resize_image(image, max_size):
    width, height = image.size
    if width <= max_size and height <= max_size:
        return image  # geen aanpassing nodig

    # verhoudingen behouden
    if width > height:
        new_width = max_size
        new_height = int(max_size * height / width)
    else:
        new_height = max_size
        new_width = int(max_size * width / height)

    return image.resize((new_width, new_height), Image.LANCZOS)

def main():
    source_dir = input("Pad naar bronmap met afbeeldingen: ").strip()
    dest_dir = input("Pad naar uitvoermap: ").strip()
    max_size = int(input("Maximale afmeting van de afbeeldingen (max 2000px): ").strip())

    if max_size > 2000:
        print("Waarschuwing: Maximale grootte is 2000 pixels. Ingesteld op 2000.")
        max_size = 2000

    if not os.path.exists(source_dir):
        print("Bronmap bestaat niet!")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    files = os.listdir(source_dir)
    image_files = [f for f in files if is_image_file(f)]
    print(f"\nAantal afbeeldingsbestanden gevonden: {len(image_files)}\n")

    for filename in files:
        filepath = os.path.join(source_dir, filename)

        if not is_image_file(filename):
            print(f"Overslaan: {filename} is geen afbeelding.")
            continue

        try:
            with Image.open(filepath) as img:
                print(f"Bezig met aanpassen: {filename}")
                resized_img = resize_image(img, max_size)
                save_path = os.path.join(dest_dir, filename)
                resized_img.save(save_path)
        except Exception as e:
            print(f"Fout bij verwerken van {filename}: {e}")

    print("\nKlaar! Aangepaste afbeeldingen zijn opgeslagen in de uitvoermap.")

if __name__ == "__main__":
    main()
