from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions instance and configure it (if needed)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Example: Enable headless mode

# Initialize the WebDriver with the options
driver = webdriver.Chrome(options=chrome_options)  # Replace with the appropriate driver for your browser

