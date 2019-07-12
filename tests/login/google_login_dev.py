import qalib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

name_of_test = "T-001-005"

description = "login prod via google"
result = []
def callback():

    login = 'assuranceq6@gmail.com'
    password = 'Secret99'
    try:

        qalib.WHICH_PLATFORM = "dev."

        browser, logs = qalib.set_up("chrome", "stdout", "false")

        qalib.load_main_page(browser, logs)
        sleep(4)
        result.append("Main page successfully opened")

    except:
        result.append("Opening main page failed")

    try:
        qalib.element_click(browser, logs, 3, By.XPATH, '//*[@id="hs-eu-confirmation-button"]')
        result.append("Cookie is accepted")
    except:
        result.append("Something wrong with cookies")

    try:

        qalib.element_click(browser, logs, 3, By.XPATH, "//h2[contains(text(),'login')]")
        sleep(2)
        qalib.element_click(browser, logs, 3, By.XPATH, "//div[@class='social-auth__icon social-auth__icon-google']")

        window_before = browser.window_handles[0]

        window_after = browser.window_handles[1]

        browser.switch_to_window(window_after)

        sleep(3)

        qalib.element_send_keys(browser, logs, 3, By.ID, "identifierId", login, Keys.ENTER)

        qalib.element_send_keys(browser, logs, 3, By.ID, "password", password, Keys.ENTER)

        browser.switch_to_window(window_before)
        sleep(4)

        qalib.wait_until_with_exception(browser, logs, 10, EC.title_is('OPN Platform'))
        sleep(4)

        result.append("Login via google successfully passed")

    except:
        result.append("Login via google failed")

    qalib.result_of_the_test(result)
    qalib.tear_down(browser, logs)
qalib.register_qa_test(name_of_test, description, callback)