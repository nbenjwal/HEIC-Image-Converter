from PIL import Image
import pillow_heif
import os


##################################################
## Author: nbenjwal
##################################################
def convert_heic(heic_path, converted_images_directory, image_format):
    if not os.path.exists(converted_images_directory):
        os.makedirs(converted_images_directory)

    pillow_heif.register_heif_opener()  # You only need to register the opener once

    for subdir, _, files in os.walk(heic_path):
        for file in files:
            if file.endswith(".HEIC"):
                file_name = os.path.join(subdir, file)
                img = Image.open(file_name)
                output_file_name = os.path.join(converted_images_directory, f"{os.path.splitext(file)[0]}." + image_format.lower())
                img.save(output_file_name, format=image_format)
                print(f"Converted: {output_file_name}")


if __name__ == "__main__":
    heic_images_directory = 'F://DCIM'              # Directory holding the HEIC images
    converted_images_directory = 'F://converted//'  # Destination directory for the converted images
    target_format = 'PNG'                           # Desired output format (options: PNG, JPEG)
    convert_heic(heic_images_directory, converted_images_directory, target_format)
