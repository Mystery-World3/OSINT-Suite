import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def scrape_metadata(url):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Analyzing Metadata from: {url} ---")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        title = soup.find('title')
        title_text = title.string.strip() if title else 'N/A'

        description = soup.find('meta', attrs={'name': 'description'})
        desc_content = description['content'].strip() if description else 'N/A'

        print(f"[+] Page Title      : {title_text}")
        print(f"[+] Meta Description: {desc_content}")
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Failed to retrieve data from URL: {e}")
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred while parsing the page: {e}")