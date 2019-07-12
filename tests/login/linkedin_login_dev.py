import qalib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from time import sleep

name_of_test = "T-002-002"

description = "login via linkedin dev"
result = []
def callback():

    login = 'tdisregard@bk.ru'
    password = 'Amsterdam99!'
    try:
        # Login via linkedin

        qalib.WHICH_PLATFORM = "dev."

        browser, logs = qalib.set_up("chrome", "stdout", "false")

        qalib.load_main_page(browser, logs)
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
        qalib.element_click(browser, logs, 3, By.XPATH, "//div[@class='social-auth__icon social-auth__icon-linkedin']")
        qalib.wait_until_with_exception(browser, logs, 10, EC.title_is('LinkedIn Login, LinkedIn Sign in | LinkedIn'))
        result.append("Page successfully forwarded to linkedin")
    except:
        result.append("Something wrong with linkedin")
    try:
        browser.find_element_by_xpath("//input[@id='username']").send_keys(login)
        browser.find_element_by_xpath("//input[@id='password']").send_keys(password)
        qalib.element_click(browser, logs, 3, By.XPATH, "//button[@class='btn__primary--large from__button--floating']")
        qalib.wait_until_with_exception(browser, logs, 10, EC.title_is('OPN Platform'))

        result.append("Login via linkedin successfully passed")
    except:
        result.append("Login via linkedin failed")

    qalib.result_of_the_test(result)
   # qalib.tear_down(browser, logs)
qalib.register_qa_test(name_of_test, description, callback)