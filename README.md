# OSINT-Suite v4.0 

A powerful and multifunctional digital investigation toolkit built with Python. This desktop application provides various tools for reconnaissance, data analysis, and automation, all wrapped in a modern, tabbed graphical user interface (GUI).


## 🌟 Features

This toolkit is organized into a clean, tabbed interface, providing a wide range of capabilities:

#### 🕵️ Identity & Network Intelligence
* **IP Locator**: Get detailed geolocation data for any IP address.
* **WHOIS Lookup**: Retrieve domain registration information.
* **Port Scanner**: Scan a target for common open network ports.
* **Username Lookup**: Check for the existence of a username across popular social media platforms.
* **Subdomain Scanner**: Discover common subdomains associated with a domain.

#### 📄 Web & Data Intelligence
* **Web Scraper**: Extract page title and meta description from a URL.
* **Table Extractor**: Scrape data tables from a webpage and export them to **CSV, Excel (.xlsx), or JSON** format using Pandas.
* **Web Capture**: Take a full-page screenshot (`.png`) or generate a PDF from any website, even dynamic, JavaScript-heavy pages, using Selenium browser automation.

#### 🔐 Forensics & Crypto Analysis
* **File Metadata Extractor**: Download and analyze `.jpg` or `.pdf` files from a URL to extract hidden metadata (EXIF data like GPS location, camera model, author info, etc.).
* **Hash Cracker**: A simple MD5/SHA1 hash cracker that uses a provided wordlist to find the original password.

#### 🎬 Multimedia Utilities
* **Media Converter**: Convert local video files (`.mp4`) into animated GIFs or extract the audio into an MP3 file using MoviePy.

#### ✨ Professional Features
* Modern, dark-themed GUI built with CustomTkinter.
* Fully-featured command-line interface (CLI) for terminal power-users.
* Ability to save the results from any tool to a `.txt` file.

## 🛠️ Technology Stack

* **Core**: Python
* **GUI**: CustomTkinter
* **Web & Network**: Requests, Sockets, python-whois
* **Browser Automation**: Selenium
* **Data Processing**: Pandas, openpyxl
* **Image/PDF Processing**: Pillow, PyPDF2
* **Multimedia**: MoviePy (with FFMPEG)
* **Packaging**: PyInstaller

## 🚀 Setup & Installation

To run this application from the source code, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mystery-World3/OSINT-Suite.git
    cd OSINT-Suite
    ```
    2.  **Create and activate a virtual environment:**
    ```bash
    # Create venv
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install FFMPEG (Required for Media Converter):**
    This tool relies on an external program, FFMPEG. Please download it from [https://ffmpeg.org/](https://ffmpeg.org/) and ensure its location is added to your system's PATH.

## 💻 How to Use

Run the GUI application with the following command:

```bash
python gui_main.py
```

Alternatively, you can use the original command-line interface:
```bash
# See all available CLI commands
python main.py --help
```

## License
This project is released under the MIT License.

*Created by Mystery-World3*
