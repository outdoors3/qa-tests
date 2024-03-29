import qalib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

name_of_test = "T-002-001"

description = "login dev testing"
result = []
def callback():

    login = 'opntesting3@gmail.com'
    password = 'Secret99'
    try:
        # Login via email

        qalib.WHICH_PLATFORM = "dev."

        browser, logs = qalib.set_up("chrome", "stdout", "false")

        qalib.load_main_page(browser, logs)

        qalib.login(browser, logs, login, password)

        #qalib.wait_until_with_exception(browser, logs, 10, EC.visibility_of_element_located((By.XPATH, "//h2[@class='MuiTypography-root-8 MuiTypography-subtitle2-20']")))

        result.append("Login via email successfully passed")
    except:
        result.append("Login via email failed")

    qalib.result_of_the_test(result)
   # qalib.tear_down(browser, logs)
qalib.register_qa_test(name_of_test, description, callback)
