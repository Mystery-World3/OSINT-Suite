import requests
from colorama import Fore, Style

def locate_ip(ip_address):
    API_URL = "http://ip-api.com/json/{}"
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Locating IP Information: {ip_address} ---")
    url = API_URL.format(ip_address)
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') == 'success':
            print(f"[+] Status    : {data['status']}")
            print(f"[+] Country   : {data.get('country', 'N/A')}")
            print(f"[+] City      : {data.get('city', 'N/A')}")
            print(f"[+] ISP       : {data.get('isp', 'N/A')}")
            print(f"[+] Organization: {data.get('org', 'N/A')}")
        else:
            print(Fore.RED + f"[!] Failed to locate IP. API Message: {data.get('message', 'Unknown')}")
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Network error while contacting API: {e}")