import whois
from datetime import datetime
from colorama import Fore, Style

def check_whois(domain):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Checking WHOIS Information for: {domain} ---")
    try:
        domain_info = whois.whois(domain)
        
        creation_date = domain_info.creation_date
        if isinstance(creation_date, list): creation_date = creation_date[0]
        expiration_date = domain_info.expiration_date
        if isinstance(expiration_date, list): expiration_date = expiration_date[0]

        print(f"[+] Domain Name   : {domain_info.domain_name}")
        print(f"[+] Registrar     : {domain_info.registrar}")
        print(f"[+] Creation Date : {creation_date.strftime('%Y-%m-%d %H:%M:%S') if creation_date else 'N/A'}")
        print(f"[+] Expiration Date: {expiration_date.strftime('%Y-%m-%d %H:%M:%S') if expiration_date else 'N/A'}")
        print(f"[+] Name Servers  : {', '.join(domain_info.name_servers) if domain_info.name_servers else 'N/A'}")
        print(f"[+] Registrant    : {domain_info.name if domain_info.name else 'Information Redacted'}")
        print(f"[+] Registrant Email: {domain_info.email if domain_info.email else 'Information Redacted'}")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to get WHOIS information. The domain may be invalid or an error occurred: {e}")