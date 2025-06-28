import socket
from datetime import datetime
from colorama import Fore, Style

def scan_ports(target):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Starting Port Scan on: {target} ---")
    try:
        target_ip = socket.gethostbyname(target)
        print(f"[*] Target IP: {target_ip}")
    except socket.gaierror:
        print(Fore.RED + f"[!] Failed to resolve host: {target}. Please check the domain or IP.")
        return

    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 993, 995, 3306, 3389, 5900, 8080, 8443]
    
    print(f"[*] Scanning {len(common_ports)} common ports...")
    start_time = datetime.now()
    open_ports = []
    
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(Fore.GREEN + f"[+] Port {port} is OPEN")
            open_ports.append(port)
        s.close()

    end_time = datetime.now()
    total_time = end_time - start_time
    
    if open_ports:
        print(Style.BRIGHT + Fore.YELLOW + f"\n[*] Finished in {total_time.total_seconds():.2f} seconds. Found {len(open_ports)} open ports.")
    else:
        print(Style.BRIGHT + Fore.YELLOW + f"\n[*] Finished. No common ports found open.")