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

    # Use CSS selectors, XPath, or other methods to extract the information you need
    # Example: Extract all product names
    product_names = response.html.find(".product-name")

    # Iterate through the product_names list and print the text content
    for product in product_names:
        print(product.text)
else:
    print(f"Request failed with status code: {response.status_code}")

