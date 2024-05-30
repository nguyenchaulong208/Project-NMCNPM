from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = ChromeService(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the webpage
url = 'https://conf.researchr.org/'
driver.get(url)

# Let the script wait for a few seconds to ensure the page is fully loaded
time.sleep(5)

# Extract content
elements = driver.find_elements(By.CSS_SELECTOR, '.navigate')
data = []
for element in elements:
    if element.text != "":
        data.append(element.text)

# Close the browser
driver.quit()

# Print the extracted data
for item in data:
    print(item)
