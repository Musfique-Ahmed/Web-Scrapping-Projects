from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_service = Service('/path/to/chromedriver')  # Update with the path to your chromedriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Function to scrape data from the phone listings
def scrape_phone_data():
    driver.get('https://gadgetandgear.com/category/phone')
    time.sleep(5)  # Wait for the page to load

    data = []

    # Find all the phone elements
    phone_elements = driver.find_elements(By.CSS_SELECTOR, 'div.product-card')

    for phone in phone_elements:
        model = phone.find_element(By.CSS_SELECTOR, 'h2.product-card__title').text.strip()
        try:
            price = phone.find_element(By.CSS_SELECTOR, 'span.product-card__price').text.strip()
        except:
            price = "Price not available"

        data.append({"Model": model, "Price": price})

    return data

# Scrape the phone data
phone_data = scrape_phone_data()

# Close the WebDriver
driver.quit()

# Save data to CSV
df = pd.DataFrame(phone_data)
df.to_csv('phone_data.csv', index=False)

print("Task Completed!!!")
