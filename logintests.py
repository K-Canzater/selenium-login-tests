from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# --- SETUP ---
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")  

# --- TEST SCENARIOS ---
def test_successful_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    try:
        driver.find_element(By.CLASS_NAME, "error-message-container")
        print("❌ Error appeared: test failed for correct credentials")
    except NoSuchElementException:
        print("✅ No error: test passed for correct credentials")

def test_wrong_password(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    
    try:
        driver.find_element(By.CLASS_NAME, "error-message-container")
        print("✅ Error appeared: test passed for wrong password")
    except NoSuchElementException:
        print("❌ No error: test failed for wrong password")


def blank_password_field(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By. ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    
    try:
        driver.find_element(By.CLASS_NAME, "error-message-container")
        print("✅ Error appeared: test passed for missing password")
    except NoSuchElementException:
        print("❌ No error: test failed for missing password")


# --- MAIN RUNNER ---
def main():
    test_successful_login(driver)
    time.sleep(2)

    test_wrong_password(driver)
    time.sleep(2)

    blank_password_field(driver)
    time.sleep(2)

    driver.quit()

if __name__ == "__main__":
    main()
