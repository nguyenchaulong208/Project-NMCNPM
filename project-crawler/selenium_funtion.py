from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_url(url):
# Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #Create object webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    time.sleep(5)
    return driver

def get_element(driver):
    # Extract content
    elements = driver.find_elements(By.CSS_SELECTOR, '.navigate')
    data = []
    for element in elements:
        if element.text != "":
            data.append(element.text)
    return data
