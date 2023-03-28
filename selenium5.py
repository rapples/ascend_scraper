import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://letsascend.com/menu/pa-wayne-menu-med/categories/5d3ff42c25bf2b9c"

headers = {
 'content-length': '12484',
 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
 'sec-ch-ua-platform': '"macOS"',
 'sec-ch-ua-mobile': '?0',
 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
 'content-type': 'application/json',
 'accept': '*/*',
 'origin': 'https://letsascend.com',
 'sec-fetch-site': 'same-origin',
 'sec-fetch-mode': 'cors',
 'sec-fetch-dest': 'empty',
 'referer': 'https://letsascend.com/menu/pa-wayne-menu-med',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'en-US,en;q=0.9',
 'cookie': '_egLastMenuVisited1=f28405257f1d1af3; dispense_prospect=29669acf-993c-4e9d-b779-6395a3996b92; _gcl_au=1.1.985409093.1679838527; _ga=GA1.2.1392991498.1679838530; _gid=GA1.2.2146267376.1679838530; _gat_gtag_UA_179717916_1=1; _gat_gtag_UA_185020359_5=1; _gat_UA-179717916-1=1; _ga_BWEQ3FJYSF=GS1.1.1679838529.1.1.1679838551.0.0.0'
}

# Set up Chrome options
chrome_options = Options()

# Set up custom headers
for header, value in headers.items():
    chrome_options.add_argument(f"--header {header}={value}")

# Initialize the Chrome webdriver with custom options
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)

# Now you can perform any operation on the page using Selenium

# https://letsascend.com/menu/pa-wayne-menu-med/categories/5d3ff42c25bf2b9c"
def extract_typography_elements(driver):
    # Find all elements with class name starting with "Typography-"
    typography_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class^="Typography-"]')

    # Iterate through the typography_elements list and print the text content
    for element in typography_elements:
        try:
            print(element.text)
        except Exception as e:
            print(f"Error while extracting element text: {e}")

# Configure the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Fetch the webpage
url = "https://letsascend.com/menu/pa-wayne-menu-med/categories/5d3ff42c25bf2b9c"
driver.get(url)

# Scroll down 10 times
scroll_count = 10
for i in range(scroll_count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Adjust the sleep time if necessary to allow the content to load
    extract_typography_elements(driver)

# Close the WebDriver
driver.quit()

