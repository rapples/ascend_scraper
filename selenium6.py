import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

# Configure the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Fetch the webpage
url = "https://letsascend.com/menu/pa-wayne-menu-med/categories/5d3ff42c25bf2b9c"
driver.get(url)

# Define the output CSV file
output_file = 'results.csv'

# Scroll down 10 times
scroll_count =5
seen_elements = set()

for x in range(scroll_count):
    print("scroll #" + str(x))
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Adjust the sleep time if necessary to allow the content to load

    # Find all elements with class name starting with "Typography-"
    typography_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class^="Typography-"]')

    # Iterate through the typography_elements list and save the text content to CSV
    for element in typography_elements:
        try:
            text = element.text
            if text not in seen_elements:
                save_to_csv([text], output_file)
                seen_elements.add(text)
            else:
                # print("repeated element "+text)
                save_to_csv([text], output_file)
        except Exception as e:
            print(f"Error while extracting element text: {e}")

# Close the WebDriver
driver.quit()

