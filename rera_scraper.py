from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Update this path to your actual ChromeDriver location
CHROMEDRIVER_PATH = "/Users/apple/Downloads/chromedriver-mac-arm64/chromedriver"

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: runs in background without opening browser
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
    url = "https://rera.odisha.gov.in/projects/project-list"
    driver.get(url)

    # Wait for the table to load
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table-bordered tbody tr")))

    # Get first 6 project rows
    rows = driver.find_elements(By.CSS_SELECTOR, "table.table-bordered tbody tr")[:6]
    projects = []

    for idx, row in enumerate(rows, start=1):
        view_link = row.find_element(By.LINK_TEXT, "View Details")
        driver.execute_script("arguments[0].scrollIntoView();", view_link)
        view_link.click()

        # Wait for RERA Regd No
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Rera Regd. No')]/following-sibling::div")))

        rera_reg_no = driver.find_element(By.XPATH, "//label[contains(text(),'Rera Regd. No')]/following-sibling::div").text.strip()
        project_name = driver.find_element(By.XPATH, "//label[contains(text(),'Project Name')]/following-sibling::div").text.strip()

        # Switch to Promoter Details tab
        promoter_tab = driver.find_element(By.ID, "promoter-tab")
        promoter_tab.click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Company Name')]/following-sibling::div")))
        promoter_name = driver.find_element(By.XPATH, "//label[contains(text(),'Company Name')]/following-sibling::div").text.strip()
        promoter_address = driver.find_element(By.XPATH, "//label[contains(text(),'Registered Office Address')]/following-sibling::div").text.strip()
        gst_no = driver.find_element(By.XPATH, "//label[contains(text(),'GST No')]/following-sibling::div").text.strip()

        # Store data
        projects.append({
            "Rera Regd. No": rera_reg_no,
            "Project Name": project_name,
            "Promoter Name": promoter_name,
            "Promoter Address": promoter_address,
            "GST No": gst_no
        })

        print(f"\nProject {idx}:")
        for key, value in projects[-1].items():
            print(f"  {key}: {value}")

        print("-" * 50)

        # Go back to project list
        driver.back()
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table-bordered tbody tr")))
        time.sleep(1)

finally:
    driver.quit()

