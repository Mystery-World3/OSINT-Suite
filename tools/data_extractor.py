import pandas as pd
import requests
import io
from colorama import Fore, Style

def extract_and_save_tables(url, output_path):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Extracting Tables from: {url[:50]}... ---")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        tables = pd.read_html(io.StringIO(requests.get(url, headers=headers).text))
        
        if not tables:
            print(Fore.RED + "[!] No tables found on this page.")
            return

        print(f"[*] Found {len(tables)} tables. Selecting the largest one to save...")
        largest_table = max(tables, key=lambda df: df.size)
        
        if output_path.endswith('.csv'):
            largest_table.to_csv(output_path, index=False)
            print(Fore.GREEN + f"[+] Table successfully saved as CSV at: {output_path}")
        elif output_path.endswith('.xlsx'):
            largest_table.to_excel(output_path, index=False, engine='openpyxl')
            print(Fore.GREEN + f"[+] Table successfully saved as Excel at: {output_path}")
        elif output_path.endswith('.json'):
            largest_table.to_json(output_path, orient='records', indent=4)
            print(Fore.GREEN + f"[+] Table successfully saved as JSON at: {output_path}")
        else:
            print(Fore.RED + f"[!] Unsupported output format. Please use .csv, .xlsx, or .json")
    except ValueError:
        print(Fore.RED + f"[!] ValueError: No tables could be parsed from the URL.")
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred: {e}")