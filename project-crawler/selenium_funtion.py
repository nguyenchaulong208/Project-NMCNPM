from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import data_meeting


def get_url(url):
# Setup Chrome options
 #Web thuan json => dung browser de truy cap vao trang web va lay du lieu ve
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #Create object webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    #Su dung gia lap chrome de truy cap vao trang web
    driver.get(url)
    time.sleep(5)
    return driver

    
# Get element
def get_element(driver):
    # Extract content
    #tao mang de chua du lieu cac thong tin cua meeting theo object cua class InfoMeeting
    data = []
    #Tim tat ca cac the <tr> trong the <table>
    getConfer = driver.find_elements(By.TAG_NAME, 'tr')
    #Voi moi the <tr> tim duoc ta tiep tuc tim cac the con ben trong the <tr> do va lay ra cac thong tin cua meeting theo object cua class InfoMeeting: .navigate, strong, a
    #Sau do luu vao mang data
    for item in getConfer:
       if item.text != "":
           getData = data_meeting.InfoMeeting()
           cofer = item.find_element(By.CSS_SELECTOR,'.navigate')
           getData.conference = cofer.text
           loca= item.find_element(By.TAG_NAME,'strong')
           getData.location = loca.text
           date = item.find_element(By.TAG_NAME,'strong')
           getData.date = date.text
           get_url = item.find_element(By.TAG_NAME,'a')
           getData.url = get_url.get_attribute('href') #Lay duong link cua the <a>
           data.append(getData)
    
    return data
