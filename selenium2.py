import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
for _ in range(scroll_count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Adjust the sleep time if necessary to allow the content to load

# Wait for the page to load (adjust the timeout as needed)
timeout = 10
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class^="Typography-"]')))

# Find all elements with class name starting with "Typography-"
typography_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class^="Typography-"]')

# Iterate through the typography_elements list and print the text content
for element in typography_elements:
    print(element.text)

# Close the WebDriver
driver.quit()

