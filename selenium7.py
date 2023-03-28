import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def print_entry(entry):
    for i, field in enumerate(entry):
        if i == 0 or field=="":
            print(field, end="")
        else:
            print(", " + field, end="")
    print("")

# Configure the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Fetch the webpage
url = "https://letsascend.com/menu/pa-wayne-menu-med/categories/5d3ff42c25bf2b9c"
driver.get(url)

# Scroll down 10 times
scroll_count = 5
seen_elements = set()

for x in range(scroll_count):
    print("running #"+str(x+1))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Adjust the sleep time if necessary to allow the content to load

    # Wait for the page to load (adjust the timeout as needed)
    timeout = 10
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class^="Typography-"]')))

    # Find all elements with class name starting with "Typography-"
    typography_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class^="Typography-"]')

    # Iterate through the typography_elements list and print the text content
    entry = []
    laststate=0
    for element in typography_elements:
        try:
            element_id = element.get_attribute("outerHTML")
            if 1==1:
                text = element.text

                # Print the entry on a single line when a price is encountered
                if text.startswith('$'):
                    if laststate!=1:
                        entry.append(text)
                        laststate=1
                    else:
                        laststate=0
                        entry.append(text)
                        print_entry(entry)
                        entry = []
                else:
                    if laststate==1:
                        if text.strip() != "NEW":
                             print_entry(entry)
                             entry = []
                             laststate=0
                        else:
                             entry = []
                             laststate=0
                        
                    else:
                        if text.strip() != "NEW":
                             entry.append(text)
                             laststate=2
        except Exception as e:
            print(f"Error while extracting element text: {e}")

# Close the WebDriver
driver.quit()


