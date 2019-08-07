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

        # try:
        #     lib.wait_until_with_exception(browser, logs, lib.DEFAULT_TIMEOUT,
        #                                   EC.text_to_be_present_in_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[2]', "User is already signed with another authorization type"))
        #     print("Passed")
        # except Exception:
        #     pass

        # lib.wait_until_with_exception(browser, logs, lib.DEFAULT_TIMEOUT,
        #                              EC.text_to_be_present_in_element(By.XPATH, "//h2[@class='MuiTypography-root MuiTypography-h5']", "Company info"))


        sleep(5)
        lib.element_send_keys(browser, logs, lib.DEFAULT_SLEEP, By.NAME, 'companyName', 'Test Registration')
        lib.element_send_keys(browser, logs, lib.DEFAULT_SLEEP, By.NAME, 'companyDescription', 'Just for test')
        s2 = browser.find_element_by_id("select-country")
        print(s2.options)
        for opt in s1.options:
            s1.select_by_visible_text('Europe')
        lib.element_send_keys(browser, logs, lib.DEFAULT_SLEEP, By.NAME, 'address', 'Test Street')
        lib.element_send_keys(browser, logs, lib.DEFAULT_SLEEP, By.NAME, 'email', 'qassurance211@gmail.com')
        lib.element_click(browser, logs, lib.DEFAULT_SLEEP, By.XPATH, "//div[@class='register-company_container']//form")



    print(social_login + ' Registration test finished successfully', file=logs)
    result = [social_login + ' registration test finished successfully']
    lib.result_of_the_test(result)
    lib.tear_down(browser, logs)


lib.register_qa_test("T-003-006", "Registration with google", callback)