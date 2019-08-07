import qalib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

name_of_test = "T-003-002"

description = "password recovery"
result = []
def callback():

    # login = 'qassurance211@gmail.com'
    # gpassword = 'Secret99'
    try:

        qalib.WHICH_PLATFORM = ""

        browser, logs = qalib.set_up("chrome", "stdout", "false")

        qalib.load_main_page(browser, logs)
        result.append("Success")
    except:
        result.append("Fail")

    try:
        qalib.element_click(browser, logs, 3, By.XPATH, '//*[@id="hs-eu-confirmation-button"]')
        result.append("Cookie is accepted")
    except:
        result.append("Something wrong with cookies")


    qalib.element_click(browser, logs, qalib.DEFAULT_SLEEP, By.XPATH, "//h2[contains(text(),'login')]")
    qalib.element_click(browser, logs, qalib.DEFAULT_SLEEP, By.CLASS_NAME, 'MuiTypography-root MuiTypography-caption MuiTypography-colorPrimary')
    print('Clicking forgot-password button..')
    initial_handle = browser.current_window_handle

    qalib.element_send_keys(browser, logs, qalib.DEFAULT_SLEEP, By.ID, 'outlined-helperText', 'qassurance211@gmail.com')



    qalib.result_of_the_test(result)
    qalib.tear_down(browser, logs)
qalib.register_qa_test(name_of_test, description, callback)


