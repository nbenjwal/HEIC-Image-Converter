from PIL import Image
import pillow_heif
import os


def convert_heic_to_png(heic_path, png_path):
    if not os.path.exists(png_path):
        os.makedirs(png_path)

    pillow_heif.register_heif_opener()  # You only need to register the opener once

    for subdir, _, files in os.walk(heic_path):
        for file in files:
            if file.endswith(".HEIC"):
                file_name = os.path.join(subdir, file)
                img = Image.open(file_name)
                output_file_name = os.path.join(png_path, f"{os.path.splitext(file)[0]}.png")
                img.save(output_file_name, format='PNG')
                print(f"Converted: {output_file_name}")


if __name__ == "__main__":
    heic_path = 'F://DCIM'
    png_path = 'F://png//'
    convert_heic_to_png(heic_path, png_path)
