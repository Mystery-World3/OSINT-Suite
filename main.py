# main.py
import argparse
from colorama import init

# Impor semua fungsi dari toolkit Anda
from tools.user_checker import check_username
from tools.ip_locator import locate_ip
from tools.web_scraper import scrape_metadata
from tools.whois_checker import check_whois
from tools.subdomain_finder import find_subdomains
from tools.port_scanner import scan_ports
from tools.hash_cracker import crack_hash
from tools.web_automator import capture_website
from tools.data_extractor import extract_and_save_tables
from tools.multimedia_converter import convert_media

def main():
    # Inisialisasi Colorama
    init(autoreset=True)
    
    # Setup Parser Argumen
    parser = argparse.ArgumentParser(
        description="OSINT-Suite v3.0: Sebuah Toolkit Investigasi Digital Multifungsi.",
        epilog="Gunakan 'python main.py --help' untuk melihat semua opsi."
    )
    
    # --- Kumpulan Definisi Argumen ---
    parser.add_argument('--username', type=str, help='Mencari akun berdasarkan username.')
    parser.add_argument('--ip', type=str, help='Mencari informasi geolokasi dari sebuah alamat IP.')
    parser.add_argument('--url', type=str, help='Mengambil metadata (judul & deskripsi) dari sebuah URL.')
    parser.add_argument('--domain', type=str, help='Mendapatkan informasi WHOIS dari sebuah domain.')
    parser.add_argument('--subdomain-scan', type=str, help='Mencari subdomain umum dari sebuah domain.')
    parser.add_argument('--port-scan', type=str, help='Memindai port umum yang terbuka pada target.')
    parser.add_argument('--crack-hash', type=str, help='Mencoba memecahkan hash MD5/SHA1.')
    parser.add_argument('--wordlist', type=str, default='wordlist.txt', help='Path ke file wordlist (default: wordlist.txt).')
    parser.add_argument('--screenshot', type=str, help='URL target untuk diambil screenshot atau diubah ke PDF.')
    parser.add_argument('--scrape-table', type=str, help='URL target untuk diekstrak tabel datanya.')
    parser.add_argument('--convert', type=str, help='Path ke file video input yang akan dikonversi.')
    parser.add_argument('--output', type=str, help='Nama file output (contoh: hasil.png atau data.csv).')
    parser.add_argument('--file-meta', type=str, help='URL ke file untuk diekstrak metadatanya.')

    # Parsing argumen dari command line
    args = parser.parse_args()

    # --- Logika Pemilihan Modul ---
    if args.convert and args.output:
        convert_media(args.convert, args.output)
    elif args.screenshot and args.output:
        capture_website(args.screenshot, args.output)
    elif args.scrape_table and args.output:
        extract_and_save_tables(args.scrape_table, args.output)
    elif args.username:
        check_username(args.username)
    elif args.ip:
        locate_ip(args.ip)
    elif args.url:
        scrape_metadata(args.url)
    elif args.domain:
        check_whois(args.domain)
    elif args.subdomain_scan:
        find_subdomains(args.subdomain_scan)
    elif args.port_scan:
        scan_ports(args.port_scan)
    elif args.crack_hash:
        crack_hash(args.crack_hash, args.wordlist)
    elif args.file_meta:
        from tools.file_meta_extractor import extract_file_metadata
        extract_file_metadata(args.file_meta)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()