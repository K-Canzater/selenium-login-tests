Automation scripts for testing login scenarios on [SauceDemo](https://www.saucedemo.com).  
This project demonstrates hands-on QA and basic Selenium skills.

## Test Scenarios

1. **Successful login** – Verifies that a valid user can log in without error messages.  
2. **Wrong password** – Verifies that an error message appears when the password is incorrect.  
3. **Blank password** – Verifies that an error message appears when the password field is empty.

## Tech Stack

- **Python 3.11**  
- **Selenium 4.x**  
- **Chrome WebDriver**

# 1. Clone repo
git clone https://github.com/K-Canzater/selenium-login-tests.git
cd selenium-login-tests

# 2. Install dependencies
pip install selenium

# 3. Run the test script
python testscript.py
