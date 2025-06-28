import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Style

def capture_website(url, output_path):
    print(Style.BRIGHT + Fore.YELLOW + f"\n--- Starting Browser Automation for: {url} ---")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--hide-scrollbars")

    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print(f"[*] Opening page...")
        driver.get(url)
        time.sleep(3)
        
        if output_path.endswith('.png'):
            print(f"[*] Taking screenshot and saving to: {output_path}")
            driver.save_screenshot(output_path)
            print(Fore.GREEN + f"[+] Screenshot saved successfully!")
        elif output_path.endswith('.pdf'):
            print(f"[*] Converting page to PDF and saving to: {output_path}")
            pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {})
            with open(output_path, 'wb') as f:
                f.write(base64.b64decode(pdf_data['data']))
            print(Fore.GREEN + f"[+] PDF saved successfully!")
        else:
            print(Fore.RED + f"[!] Unsupported output format. Please use .png or .pdf")
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred during browser automation: {e}")
    finally:
        print("[*] Closing browser...")
        driver.quit()