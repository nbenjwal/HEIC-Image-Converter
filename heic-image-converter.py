from PIL import Image
import pillow_heif
import os

##################################################
## Author: nbenjwal
##################################################
def convert_heic(heic_path, png_path, image_format):


    if not os.path.exists(png_path):
        os.makedirs(png_path)

    pillow_heif.register_heif_opener()  # You only need to register the opener once

    for subdir, _, files in os.walk(heic_path):
        for file in files:
            if file.endswith(".HEIC"):
                file_name = os.path.join(subdir, file)
                img = Image.open(file_name)
                output_file_name = os.path.join(png_path, f"{os.path.splitext(file)[0]}."+image_format.lower())
                img.save(output_file_name, format=image_format)
                print(f"Converted: {output_file_name}")


if __name__ == "__main__":
    heic_images_path = 'F://DCIM'  # Path for HEIC format images
    output_path = 'F://converted//'  # Path for converted images
    required_image_format = 'JPEG'  # Supported: PNG, JPEG
    convert_heic(heic_images_path, output_path, required_image_format)
