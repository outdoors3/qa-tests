from time import sleep
import qalib as lib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

GOOGLE = 1

Googleuser = 'qassurance211@gmail.com'


def callback():

    social_login = "google"
    headless_flag = "false"
    lib.WHICH_PLATFORM = ""
    logs_pipe = "stdout"
    browser_flag = "chrome"

    if headless_flag not in ['false', 'true']\
            or lib.WHICH_PLATFORM not in ['dev',  '']\
            or browser_flag not in ['chrome', 'firefox']:  # TODO
        print('Incorrect argument(-s)')
        exit(lib.CODE_INCORRECT_ARGUMENTS)

    if headless_flag == 'false':
        headless_flag = False
    elif headless_flag == 'true':
        headless_flag = True

    browser, logs = lib.set_up(browser_flag, logs_pipe, headless_flag)

    lib.load_register_main_page(browser, logs)

    initial_handle = browser.current_window_handle

    lib.element_click(browser, logs, 3, By.XPATH, '//*[@id="hs-eu-confirmation-button"]')


    lib.element_click(browser, logs, 3, By.XPATH, "//div[@class='social-auth__icon social-auth__icon-google']")

    lib.wait_until_with_exception(browser, logs, lib.DEFAULT_TIMEOUT, EC.number_of_windows_to_be(2))

    for handle in browser.window_handles:
        if handle == initial_handle:
            continue

        sleep(3)

        browser.switch_to.window(handle)

        lib.wait_until_with_exception(browser, logs, lib.DEFAULT_TIMEOUT,
                                      EC.title_contains('Вход'))
        lib.element_send_keys(browser, logs, lib.DEFAULT_SLEEP, By.XPATH, '//*[@id="identifierId"]', 'qassurance211@gmail.com',
                              Keys.TAB, Keys.TAB, Keys.ENTER)

        lib.wait_until_with_exception(browser, logs, lib.DEFAULT_TIMEOUT,
                                      EC.visibility_of_element_located(
                                          (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        lib.element_send_keys(browser, logs, lib.DEFAULT_SLEEP,  By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input',
                              'Amsterdam99!', Keys.ENTER)

        browser.switch_to_window(initial_handle)
        sleep(5)
        lib.element_click(browser, logs, lib.DEFAULT_SLEEP, By.XPATH, "	//span[@class='MuiButton-label']")
        sleep(5)



    print(social_login + ' Registration test finished successfully', file=logs)
    result = [social_login + ' registration test finished successfully']
    lib.result_of_the_test(result)
    lib.tear_down(browser, logs)


lib.register_qa_test("T-003-007", "Registration with google", callback)