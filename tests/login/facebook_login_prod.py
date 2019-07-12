import qalib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from time import sleep

name_of_test = "T-001-003"

description = "login prod via facebook"
result = []
def callback():

    login = 'test.rrr@bk.ru'
    password = 'Amsterdam99!'
    try:

        qalib.WHICH_PLATFORM = ""

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
        qalib.element_click(browser, logs, 3, By.XPATH, "//div[@class='social-auth__icon social-auth__icon-facebook']")

        window_before = browser.window_handles[0]

        window_after = browser.window_handles[1]

        browser.switch_to_window(window_after)

        qalib.element_send_keys(browser, logs, 3, By.ID, "email", login)

        qalib.element_send_keys(browser, logs, 3, By.ID, "pass", password)

        qalib.element_click(browser, logs, 3, By.NAME, value="login")


        browser.switch_to_window(window_before)
        sleep(4)

        qalib.wait_until_with_exception(browser, logs, 10, EC.title_is('OPN Platform'))
        sleep(4)

        result.append("Login via facebook successfully passed")

    except:
        result.append("Login via facebook failed")

    qalib.result_of_the_test(result)
    qalib.tear_down(browser, logs)
qalib.register_qa_test(name_of_test, description, callback)
