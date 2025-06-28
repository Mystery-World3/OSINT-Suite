import requests
from colorama import Fore, Style

def find_subdomains(domain):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Starting Subdomain Scan for: {domain} ---")

    subdomain_list = [
        'www', 'mail', 'ftp', 'localhost', 'api', 'dev', 'test', 'blog',
        'shop', 'store', 'vpn', 'm', 'support', 'docs', 'admin', 'portal',
        'app', 'assets', 'static', 'cdn'
    ]
    
    found_subdomains = []
    
    for subdomain in subdomain_list:
        url = f"https://{subdomain}.{domain}"
        try:
            requests.get(url, timeout=3)
            print(Fore.GREEN + f"[+] Found: {url}")
            found_subdomains.append(url)
        except requests.ConnectionError:
            pass
        except Exception as e:
            pass

    if not found_subdomains:
        print(Fore.YELLOW + "\n[*] No common subdomains found.")
    else:
        print(Style.BRIGHT + Fore.YELLOW + f"\n[*] Finished. Found {len(found_subdomains)} subdomains.")