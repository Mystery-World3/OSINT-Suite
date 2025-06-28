# gui_main.py
import customtkinter
import io
import sys
import re
from tkinter import filedialog

from tools.ip_locator import locate_ip
from tools.whois_checker import check_whois
from tools.port_scanner import scan_ports
from tools.user_checker import check_username
from tools.web_scraper import scrape_metadata
from tools.subdomain_finder import find_subdomains
from tools.hash_cracker import crack_hash
from tools.web_automator import capture_website
from tools.data_extractor import extract_and_save_tables
from tools.multimedia_converter import convert_media

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("OSINT-Suite v4.0 - The Professional")
        self.geometry("900x700")
        self.minsize(800, 600)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tab_view = customtkinter.CTkTabview(self, segmented_button_fg_color="#1F6AA5")
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.tab_view.add("IP Locator")
        self.tab_view.add("WHOIS Lookup")
        self.tab_view.add("Port Scanner")
        self.tab_view.add("Username Lookup")
        self.tab_view.add("Subdomain Scanner")
        self.tab_view.add("Web Scraper")
        self.tab_view.add("Hash Cracker")
        self.tab_view.add("Web Capture")
        self.tab_view.add("Table Extractor")
        self.tab_view.add("Media Converter")

        self.setup_ip_locator_tab()
        self.setup_whois_checker_tab()
        self.setup_port_scanner_tab()
        self.setup_username_checker_tab()
        self.setup_subdomain_scanner_tab()
        self.setup_web_scraper_tab()
        self.setup_hash_cracker_tab()
        self.setup_web_capture_tab()
        self.setup_data_extractor_tab()
        self.setup_media_converter_tab()

    def setup_single_input_tab(self, tab_name, placeholder, button_text, command):
        tab = self.tab_view.tab(tab_name)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(1, weight=1)

        button_frame = customtkinter.CTkFrame(tab, fg_color="transparent")
        button_frame.grid(row=0, column=1, padx=20, pady=10)

        entry = customtkinter.CTkEntry(tab, placeholder_text=placeholder)
        entry.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        
        button = customtkinter.CTkButton(button_frame, text=button_text, command=command)
        button.pack(side="left", padx=(0, 10))
        
        textbox = customtkinter.CTkTextbox(tab, state="disabled", font=("Consolas", 12))
        textbox.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        save_button = customtkinter.CTkButton(button_frame, text="Save Results", command=lambda tb=textbox: self.save_results(tb))
        save_button.pack(side="left")
        
        return entry, textbox

    def setup_double_input_tab(self, tab_name, placeholder1, placeholder2, button_text, command):
        tab = self.tab_view.tab(tab_name)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(2, weight=1)
        
        input_frame = customtkinter.CTkFrame(tab)
        input_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(0, weight=1)

        entry1 = customtkinter.CTkEntry(input_frame, placeholder_text=placeholder1)
        entry1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        entry2 = customtkinter.CTkEntry(input_frame, placeholder_text=placeholder2)
        entry2.grid(row=1, column=0, padx=10, pady=(0,10), sticky="ew")

        button = customtkinter.CTkButton(tab, text=button_text, command=command)
        button.grid(row=1, column=0, columnspan=2, padx=20, pady=5)
        
        textbox = customtkinter.CTkTextbox(tab, state="disabled", font=("Consolas", 12))
        textbox.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        
        return entry1, entry2, textbox

    def setup_ip_locator_tab(self):
        self.ip_entry, self.ip_textbox = self.setup_single_input_tab("IP Locator", "Enter an IP address...", "Locate IP", self.run_ip_locator_tool)

    def setup_whois_checker_tab(self):
        self.whois_entry, self.whois_textbox = self.setup_single_input_tab("WHOIS Lookup", "Enter a domain name...", "Lookup WHOIS", self.run_whois_tool)

    def setup_port_scanner_tab(self):
        self.port_entry, self.port_textbox = self.setup_single_input_tab("Port Scanner", "Enter a domain or IP target...", "Scan Ports", self.run_port_scanner_tool)

    def setup_username_checker_tab(self):
        self.user_entry, self.user_textbox = self.setup_single_input_tab("Username Lookup", "Enter a username...", "Check Username", self.run_username_checker_tool)

    def setup_subdomain_scanner_tab(self):
        self.subdomain_entry, self.subdomain_textbox = self.setup_single_input_tab("Subdomain Scanner", "Enter a domain (e.g., google.com)...", "Scan Subdomains", self.run_subdomain_scanner_tool)

    def setup_web_scraper_tab(self):
        self.webscrape_entry, self.webscrape_textbox = self.setup_single_input_tab("Web Scraper", "Enter a website URL...", "Scrape Metadata", self.run_web_scraper_tool)

    def setup_hash_cracker_tab(self):
        tab = self.tab_view.tab("Hash Cracker")
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(2, weight=1)
        
        self.hash_entry, self.wordlist_entry, self.hash_textbox = self.setup_double_input_tab("Hash Cracker", "Enter a hash...", "Wordlist path (default: wordlist.txt)", "Crack Hash", self.run_hash_cracker_tool)
        self.wordlist_entry.insert(0, "wordlist.txt")

    def setup_web_capture_tab(self):
        self.ss_url_entry, self.ss_output_entry, self.ss_textbox = self.setup_double_input_tab("Web Capture", "Enter target URL...", "Output file name (e.g., capture.png or report.pdf)", "Capture Page", self.run_screenshot_tool)
    
    def setup_data_extractor_tab(self):
        self.de_url_entry, self.de_output_entry, self.de_textbox = self.setup_double_input_tab("Table Extractor", "Enter URL with a data table...", "Output file name (e.g., data.csv or data.xlsx)", "Extract Table", self.run_data_extractor_tool)

    def setup_media_converter_tab(self):
        self.mc_input_entry, self.mc_output_entry, self.mc_textbox = self.setup_double_input_tab("Media Converter", "Input video file path (e.g., video.mp4)...", "Output file name (e.g., animation.gif or audio.mp3)", "Convert Media", self.run_media_converter_tool)

    def clean_ansi_codes(self, text):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def save_results(self, textbox_widget):
        content = textbox_widget.get("1.0", "end-1c")
        if not content.strip(): return
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if filepath:
            try:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
            except Exception as e:
                self.show_error_in_textbox(textbox_widget, f"Failed to save file: {e}")

    def show_error_in_textbox(self, textbox, message):
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("1.0", message)
        textbox.configure(state="disabled")

    def run_in_background(self, tool_function, output_textbox, *args):
        output_textbox.configure(state="normal")
        output_textbox.delete("1.0", "end")
        output_textbox.insert("1.0", f"--- Processing request... Please wait. ---")
        output_textbox.configure(state="disabled")
        self.update_idletasks()

        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        
        try:
            tool_function(*args)
        except Exception as e:
            print(f"A fatal error occurred while running the tool: {e}")

        sys.stdout = sys.__stdout__
        
        raw_output = output_buffer.getvalue()
        clean_output = self.clean_ansi_codes(raw_output)
        
        self.show_error_in_textbox(output_textbox, clean_output)

    def run_ip_locator_tool(self): self.run_in_background(locate_ip, self.ip_textbox, self.ip_entry.get())
    def run_whois_tool(self): self.run_in_background(check_whois, self.whois_textbox, self.whois_entry.get())
    def run_port_scanner_tool(self): self.run_in_background(scan_ports, self.port_textbox, self.port_entry.get())
    def run_username_checker_tool(self): self.run_in_background(check_username, self.user_textbox, self.user_entry.get())
    def run_subdomain_scanner_tool(self): self.run_in_background(find_subdomains, self.subdomain_textbox, self.subdomain_entry.get())
    def run_web_scraper_tool(self): self.run_in_background(scrape_metadata, self.webscrape_textbox, self.webscrape_entry.get())
    def run_hash_cracker_tool(self): self.run_in_background(crack_hash, self.hash_textbox, self.hash_entry.get(), self.wordlist_entry.get())
    def run_screenshot_tool(self): self.run_in_background(capture_website, self.ss_textbox, self.ss_url_entry.get(), self.ss_output_entry.get())
    def run_data_extractor_tool(self): self.run_in_background(extract_and_save_tables, self.de_textbox, self.de_url_entry.get(), self.de_output_entry.get())
    def run_media_converter_tool(self): self.run_in_background(convert_media, self.mc_textbox, self.mc_input_entry.get(), self.mc_output_entry.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()