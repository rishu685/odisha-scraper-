
# RERA Odisha Project Scraper

This Python script scrapes the first 6 projects listed on the "Projects Registered" page of the RERA Odisha website.

## 🔗 URL Scraped
https://rera.odisha.gov.in/projects/project-list

## 📋 Extracted Fields
- RERA Regd. No
- Project Name
- Promoter Name (Company Name under Promoter Details Tab)
- Address of the Promoter (Registered Office Address)
- GST No.

## 🧰 Requirements
- Python 3.7+
- Google Chrome (Matching version with ChromeDriver)
- Google ChromeDriver

## 📦 Installation

1. **Install Python packages:**
```bash
pip install selenium beautifulsoup4
```

2. **Download ChromeDriver:**
   - Match the version of Chrome installed on your system.
   - Download from: https://googlechromelabs.github.io/chrome-for-testing/

3. **Unzip and Move ChromeDriver:**
```bash
unzip chromedriver-mac-arm64.zip
chmod +x chromedriver-mac-arm64/chromedriver
sudo mv chromedriver-mac-arm64/chromedriver /usr/local/bin/chromedriver
```

4. **Set Chrome Binary Location (if needed):**
If Chrome isn't found, specify the path in your script:
```python
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

## ▶️ Run the Script
```bash
python3 rera_scraper.py
```

The script will launch Chrome, scrape the details of the first 6 projects, and print the results in the terminal.

## 📁 Output
Project details are printed in the console.
