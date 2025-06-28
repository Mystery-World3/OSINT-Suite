import hashlib
from colorama import Fore, Style

def crack_hash(target_hash, wordlist_path):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Starting Hash Crack: {target_hash[:20]}... ---")
    
    hash_length = len(target_hash)
    if hash_length == 32:
        hash_algorithm = 'md5'
    elif hash_length == 40:
        hash_algorithm = 'sha1'
    else:
        print(Fore.RED + f"[!] Unknown hash type. Only MD5 (32 chars) and SHA1 (40 chars) are supported.")
        return

    print(f"[*] Hash type detected: {hash_algorithm.upper()}")
    
    try:
        with open(wordlist_path, 'r', errors='ignore') as f:
            print(f"[*] Using wordlist from: {wordlist_path}")
            for line in f:
                word = line.strip()
                hashed_word = hashlib.new(hash_algorithm, word.encode()).hexdigest()
                if hashed_word == target_hash:
                    print(Style.BRIGHT + Fore.GREEN + f"\n[+] HASH CRACKED! The password is: {word}")
                    return
    except FileNotFoundError:
        print(Fore.RED + f"[!] Error: Wordlist file not found at '{wordlist_path}'")
        return
        
    print(Fore.YELLOW + "\n[*] Finished. Password not found in this wordlist.")