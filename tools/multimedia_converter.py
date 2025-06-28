from moviepy.editor import VideoFileClip
from colorama import Fore, Style

def convert_media(input_path, output_path):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Starting Media Conversion for: {input_path} ---")
    try:
        print("[*] Loading video file...")
        video = VideoFileClip(input_path)
        
        if output_path.endswith('.gif'):
            print(f"[*] Converting to GIF... This might take a moment and use high CPU.")
            video.write_gif(output_path, fps=10)
            print(Fore.GREEN + f"[+] GIF successfully created at: {output_path}")
        elif output_path.endswith('.mp3'):
            print(f"[*] Extracting audio to MP3...")
            audio = video.audio
            audio.write_audiofile(output_path)
            audio.close()
            print(Fore.GREEN + f"[+] MP3 successfully created at: {output_path}")
        else:
            print(Fore.RED + f"[!] Unsupported output format. Please use .gif or .mp3")

        video.close()
    except FileNotFoundError:
        print(Fore.RED + f"[!] Error: Input file not found at '{input_path}'")
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred during conversion. Please ensure FFMPEG is correctly installed. Error: {e}")