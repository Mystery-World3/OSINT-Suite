import requests
import io
from PIL import Image
from PIL.ExifTags import TAGS
from PyPDF2 import PdfReader
from colorama import Fore, Style

def extract_image_meta(file_in_memory):
    try:
        image = Image.open(file_in_memory)
        exif_data = image._getexif()

        if not exif_data:
            print(Fore.YELLOW + "[*] No EXIF data found in this image.")
            return

        print(Fore.GREEN + "[+] EXIF Data Found:")
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if tag_name in ['Make', 'Model', 'DateTimeOriginal', 'GPSInfo']:
                print(f"    {tag_name:16}: {value}")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to process image metadata: {e}")

def extract_pdf_meta(file_in_memory):
    try:
        reader = PdfReader(file_in_memory)
        meta = reader.metadata

        if not meta:
            print(Fore.YELLOW + "[*] No metadata found in this PDF.")
            return

        print(Fore.GREEN + "[+] PDF Metadata Found:")
        print(f"    Title    : {meta.title}")
        print(f"    Author   : {meta.author}")
        print(f"    Subject  : {meta.subject}")
        print(f"    Creator  : {meta.creator} (Software)")
        print(f"    Producer : {meta.producer} (PDF Software)")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to process PDF metadata: {e}")

def extract_file_metadata(url):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Analyzing File Metadata from URL: {url[:50]}... ---")
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        content_type = response.headers.get('content-type', '').lower()
        print(f"[*] File type detected: {content_type}")

        file_in_memory = io.BytesIO(response.content)

        if 'image' in content_type:
            extract_image_meta(file_in_memory)
        elif 'pdf' in content_type:
            extract_pdf_meta(file_in_memory)
        else:
            print(Fore.RED + f"[!] File type '{content_type}' is not supported by this module.")
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Failed to download file from URL: {e}")