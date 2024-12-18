from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # Open the infinite scrolling page
    driver.get("https://blog.hubspot.com/website/website-pop-up-examples")

    cookie_banner = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "hs-eu-cookie-confirmation"))
    )
    cookie_banner.click(By.ID, "hs-eu-confirmation-button")
    print("Successfully clicked on the 'Accep Cookies' Button!")

    blog_signup = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS, "blog-exit-intent-modal cl-modal-main"))
    )
    blog_signup.click(By.CLASS, "blog-exit-intent-header-close")
    print("Successfully clicked on the 'X' Button in the pop up!")


    # Optionally, wait to observe the result
    time.sleep(100)



finally:
    # Close the browser
    driver.quit()