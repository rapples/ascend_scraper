from requests_html import HTMLSession

# Initialize the session
session = HTMLSession()

# Fetch the webpage
url = "https://letsascend.com/menu/pa-wayne-menu-med/categories/5d3ff42c25bf2b9c"
response = session.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Render the JavaScript (if necessary)
    response.html.render()

    # Find all elements with class name starting with "Typography-"
    typography_elements = response.html.find('div[class^="Typography-"]')

    # Iterate through the typography_elements list and print the text content
    for element in typography_elements:
        print(element.text)
else:
    print(f"Request failed with status code: {response.status_code}")

