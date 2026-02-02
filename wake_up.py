from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ----------------------------------------
# 1. EDIT THIS LIST WITH YOUR APP URLS
# ----------------------------------------
app_urls = [
    "https://oladipupo-david-compounder-app.streamlit.app/",
    "https://oladipupo-david-finance-dashboard.streamlit.app/"
]

# ----------------------------------------
# 2. THE REST IS AUTOMATIC
# ----------------------------------------
chrome_options = Options()
# Updated to the new headless mode for stability
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Automatically install the matching driver for the current Chrome version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

print(f"Starting wake-up cycle for {len(app_urls)} apps...")

for url in app_urls:
    try:
        print(f"Visiting: {url}")
        driver.get(url)
        time.sleep(5) # Wait for page to load
        
        # Look for the 'Yes, get this app back up' button
        buttons = driver.find_elements(By.XPATH, '//button[contains(text(), "Yes, get this app back up")]')
        
        if buttons:
            print(f"Sleep detected on {url}. Clicking wake up button...")
            buttons[0].click()
            time.sleep(10) # Wait for reload
        else:
            print(f"No sleep button found on {url} (it might be awake).")
            
    except Exception as e:
        print(f"Error checking {url}: {e}")

driver.quit()
print("Cycle complete.")
