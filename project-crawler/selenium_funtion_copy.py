import time
from selenium import webdriver
import data_meeting
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# Open the URL of the web page
driver.get("https://ccfddl.github.io/")

# Sleep to wait for the page to load completely
time.sleep(10)

# Find elements with the tag name 'tr'
getConfer = driver.find_elements(By.TAG_NAME, 'tr')

getContents = []

# Extract data
for content in getConfer:
    data = data_meeting.InfoMeeting()
    confer = content.find_element(By.CSS_SELECTOR, '.el-row')
    data.conference = confer.text
    getContents.append(data)

# Print the extracted data
for content in getContents:
    print(content.conference)

# Close the browser
driver.quit()
