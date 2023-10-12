# HEIC-to-PNG-Converter
A simple yet effective Python utility that converts iPhone's HEIC image format to the widely supported PNG format.

## Features
Batch conversion support: Convert multiple HEIC images at once.
Maintain image quality: Retains the original image quality post-conversion.
Lightweight: Minimal dependencies for a smooth user experience.

## Prerequisites
Python 3.x

## Installation
Clone the repository:
```
git clone https://github.com/nbenjwal/HEIC-to-PNG-Converter.git
```
Navigate to the project directory:
```
cd HEIC-to-PNG-Converter
```
Install required dependencies:
```
 pip install pillow_heif
```


## Usage
Before running the script, please configure the following paths in the Python code:
```
    heic_path = 'F://DCIM'  # Specify the directory containing HEIC images
    png_path = 'F://png//'  # Designate the destination directory for converted PNG images
```

Run the converter script:
```
    python heic-to-png.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.