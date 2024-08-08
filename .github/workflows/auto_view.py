from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome without a visible window
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (optional)

# Website URL to view
url = "https://videoxigj.blogspot.com/?m=1"  # Replace with your desired website

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the website
    driver.get(url)

    # Optionally, add more interactions or wait for specific elements to load
    time.sleep(10)  # Stay on the page for 10 seconds (adjust as needed)

finally:
    # Close the browser window
    driver.quit()
