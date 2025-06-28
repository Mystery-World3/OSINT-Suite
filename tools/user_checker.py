import requests
from colorama import Fore, Style

def check_username(username):
    SITES = {
        'Instagram': 'https://www.instagram.com/{}',
        'GitHub': 'https://github.com/{}',
        'Reddit': 'https://www.reddit.com/user/{}',
        'Twitter': 'https://twitter.com/{}'
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Checking Username '{username}' ---")
    found_count = 0
    
    for site, url_format in SITES.items():
        url = url_format.format(username)
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Found: Account exists on {site} -> {url}")
                found_count += 1
        except requests.RequestException as e:
            print(Fore.RED + f"[!] Error while checking {site}: {e}")
            
    if found_count == 0:
        print(Fore.YELLOW + "\n[*] No accounts found with this username.")
    else:
        print(Style.BRIGHT + Fore.YELLOW + f"\n[*] Finished. Found on {found_count} sites.")