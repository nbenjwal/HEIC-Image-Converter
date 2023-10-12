# HEIC-Image-Converter (PNG, JPEG)
A simple yet effective Python utility that converts iPhone's HEIC image format to the widely supported PNG and JPEG format.

## Features
Batch conversion support: Convert multiple HEIC images at once.
Maintain image quality: Retains the original image quality post-conversion.
Lightweight: Minimal dependencies for a smooth user experience.

## Prerequisites
Python 3.x

## Installation
Clone the repository:
```
git clone https://github.com/nbenjwal/HEIC-Image-Converter.git
```
Navigate to the project directory:
```
cd HEIC-Image-Converter
```
Install required dependencies:
```
pip install pillow_heif
```


## Usage
Before running the script, please configure the following paths in the Python code:
```
heic_images_directory = 'F://DCIM'              # Directory holding the HEIC images
converted_images_directory = 'F://converted//'  # Destination directory for the converted images
target_format = 'PNG'                           # Desired output format (options: PNG, JPEG)
```

Run the converter script:
```
python heic-image-converter.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.