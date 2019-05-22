import os
import sys
import time
import random
import string
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.chrome.options import Options
WHICH_PLATFORM = ''

CODE_INCORRECT_NO_OF_ARGUMENTS = 1
CODE_INCORRECT_ARGUMENTS = 2
CODE_TIMEOUT = 3

DEFAULT_SLEEP = 2
DEFAULT_LENGTH = 36

DEFAULT_TIMEOUT = 10

DEFAULT_USER = {
     'username': 'opntesting3@gmail.com',
     'password': 'Secret99'
}

# homepage href xpath
HOME = "//span[@class='title']"

# False, if u want test local and True for selenoid
TEST_ON_SELENOID = False

# dictionary of tests dct["index"] = [description, callback_function]
DCT_TESTS = {}


def register_qa_test(name, description, callback):
    DCT_TESTS[name] = [description, callback]


def set_up_chrome(logs_pipe, headless, *extensions):
    if logs_pipe == 'stdout':
        logs = sys.stdout
    else:
        logs = open(logs_pipe, 'a')

    if TEST_ON_SELENOID:
        chrome_options = Options()
        chrome_options.add_extension('chrome.crx')
        print()
        capabilities = {
            "browserName": "chrome",
            "version": "69.0",
            "enableVNC": True,
            "enableVideo": True,
            'userExtensions': 'chrome_options',
        }
        print(capabilities)
        chrome = webdriver.Remote(
            command_executor="",
            desired_capabilities=capabilities,
            )

        with open('session_id.txt', "w") as file:
            file.write(chrome.session_id)



    else:
        options = webdriver.ChromeOptions()

        extensions = list(extensions)
        print(date(), 'extensions:', extensions)

        if len(extensions) > 0:
            for extension in extensions:
                if len(extension) > 0:
                    extension = str(extension[0])
                    print('--extension:', extension)
                    options.add_extension(extension)

        chrome = webdriver.Chrome(os.path.abspath('chromedriver'), options=options)

    chrome.set_window_size("1920", "1080")

    return chrome, logs


def set_up_firefox(logs_pipe, headless, *extensions):
    if logs_pipe == 'stdout':
        logs = sys.stdout
    else:
        logs = open(logs_pipe, 'a')

    options = webdriver.FirefoxOptions()

    if headless:
        options.add_argument('--headless')

    profile = webdriver.FirefoxProfile()

    extensions = list(extensions)
    print('extensions:', extensions)

    if len(extensions) > 0:
        for extension in extensions:
            if len(extension) > 0:
                extension = str(extension[0])
                print('--extension:', extension)
                profile.add_extension(extension)

    firefox = webdriver.Firefox(executable_path=os.path.abspath('../geckodriver'),
                                firefox_profile=profile,
                                firefox_options=options)
    firefox.maximize_window()

    return firefox, logs


def set_up(browser, logs_pipe, headless, *extensions):
    if browser == 'chrome':
        return set_up_chrome(logs_pipe, headless, extensions)
    if browser == 'firefox':
        return set_up_firefox(logs_pipe, headless, extensions)
    return None, None


def retrieve_element(browser, logs, delay=3, by=By.XPATH, value=HOME):
    time.sleep(delay)

    print(date(), 'Starting retrieving element (by: {}, value: {})...'.format(by, value), file=logs)
    wait_until_without_exception(browser, logs, DEFAULT_TIMEOUT, EC.visibility_of_element_located((by, value)))
    print(date(), 'Element {} is located'.format(value), file=logs)

    element = browser.find_element(by, value)
    print(date(), 'Element {} retrieved'.format(value), file=logs)

    return element


def retrieve_elements(browser, logs, by=By.XPATH, value=HOME):
    print(date() + "Retrieving elements by '{}' value '{}'".format(by, value), file=logs)
    wait_until_with_exception(browser, logs, DEFAULT_TIMEOUT, EC.visibility_of_element_located((by, value)))
    print(date() + "Elements {} found".format(value), file=logs)
    elements = browser.find_elements(by, value)
    return elements


def element_click(browser, logs,
                  delay=3, by=By.XPATH,
                  value=HOME):
    print(date(), 'Retrieving element "{}" for clicking...'.format(value), file=logs)
    element = retrieve_element(browser, logs, delay, by, value)
    wait_until_without_exception(browser, logs, DEFAULT_TIMEOUT, EC.element_to_be_clickable((by, value)))

    print(date(), 'Element "{}" ready for clicking'.format(value), file=logs)

    print(date(), 'Starting click "{}"...'.format(value), file=logs)

    actions = webdriver.ActionChains(browser)

    # width_center = element.size.get('width') // 2
    # height_center = element.size.get('height') // 2

    # actions.move_to_element_with_offset(element, width_center, height_center).click().perform()
    # actions.move_to_element(element).click().perform()
    actions.move_to_element_with_offset(element, 1, 1).click().perform()

    # browser.execute_script('arguments[0].click();', element)

    print(date(), 'Clicking "{}" finished'.format(value), file=logs)

def element_send_keys_select(browser, logs, delay, by, value, *keys):
    print(date(), 'Retrieving element "{}" for sending keys...'.format(value), file=logs)
    element = retrieve_element(browser, logs, delay, by, value)
    wait_until_without_exception(browser, logs, DEFAULT_TIMEOUT, EC.element_to_be_clickable((by, value)))

    try:
        element.clear()
        element.click()
        element.clear()
    except Exception:
        pass

    print(date(), 'Element "{}" ready for sending keys'.format(value), file=logs)
    print(date(), 'Starting sending keys {}...'.format(keys), file=logs)

    # width_center = element.size.get('width') // 2
    # height_center = element.size.get('height') // 2

    actions = webdriver.ActionChains(browser)

    # actions.move_to_element_with_offset(element, width_center, height_center).send_keys(keys).perform()
    # actions.move_to_element(element).send_keys(keys).perform()
    browser.find_element(by, value).send_keys(keys)

    print(date(), 'Sending keys finished', file=logs)

def element_send_keys(browser, logs, delay, by, value, *keys):
    print(date(), 'Retrieving element "{}" for sending keys...'.format(value), file=logs)
    element = retrieve_element(browser, logs, delay, by, value)
    wait_until_without_exception(browser, logs, DEFAULT_TIMEOUT, EC.element_to_be_clickable((by, value)))

    try:
        element.clear()
        element.click()
        element.clear()
    except Exception:
        pass

    print(date(), 'Element "{}" ready for sending keys'.format(value), file=logs)
    print(date(), 'Starting sending keys {}...'.format(keys), file=logs)

    # width_center = element.size.get('width') // 2
    # height_center = element.size.get('height') // 2

    actions = webdriver.ActionChains(browser)

    # actions.move_to_element_with_offset(element, width_center, height_center).send_keys(keys).perform()
    # actions.move_to_element(element).send_keys(keys).perform()
    actions.move_to_element_with_offset(element, 1, 1).send_keys(keys).perform()

    print(date(), 'Sending keys finished', file=logs)


def wait_until_with_exception(browser, logs, duration, method):
    try:
        try:
            print(date(), 'Started waiting {}s (until_with) for "{}"...'.format(duration, method.locator), file=logs)
        except Exception as e:
            print(date(), 'Started waiting {}s (until_with) without locator:\n{}'.format(duration, e), file=logs)
        WebDriverWait(browser, duration).until(method)
        print(date(), 'Finished waiting (until_with)', file=logs)
    except TimeoutException:
        print(date(), 'Waiting exceeded duration {}s (until_with), exit...'.format(duration), TimeoutException, file=logs)
        exit(CODE_TIMEOUT)


def wait_until_without_exception(browser, logs, duration, method):
    print(date(), 'Started waiting {}s (until_without)...'.format(duration), file=logs)
    WebDriverWait(browser, duration).until(method)
    print(date(), 'Finished waiting (until_without)', file=logs)


def wait_until_not_with_exception(browser, logs, duration, method):
    try:
        print(date(), 'Started waiting {}s (until_not_with)...'.format(duration), file=logs)
        WebDriverWait(browser, duration).until_not(method)
        print(date(), 'Finished waiting (until_not_with)', file=logs)
    except TimeoutException:
        print(date(), 'Waiting exceeded duration {}s (until_not_with)'.format(duration), TimeoutException, file=logs)
        exit(CODE_TIMEOUT)


def wait_until_not_without_exception(browser, logs, duration, method):
    print(date(), 'Started waiting {}s (until_not_without)...'.format(duration), file=logs)
    WebDriverWait(browser, duration).until_not(method)
    print(date(), 'Finished waiting (until_not_without)', file=logs)


def load_main_page(browser, logs):
    main_page = 'https://' + WHICH_PLATFORM + 'opnplatform.com'
    print(date(), "Main page is '%s'" % main_page)

    browser.get(main_page)
    print(date(), 'Main page opened', file=logs)
    try:
        element = retrieve_element(browser, logs, 3, By.XPATH,
                                   '//a[contains(@class, "button-white") and contains(text(), "GO AHEAD")]')
        element.click()
    except:
        pass


def load_register_main_page(browser, logs):
    browser.get('https://' + WHICH_PLATFORM + 'opnplatform.com/register')
    print(date(), 'Main page for ' + WHICH_PLATFORM + ' opened', file=logs)



def login(browser, logs, username, password):
    element_click(browser, logs, DEFAULT_SLEEP, By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[2]/a[1]/div/button')
    print(date(), 'Starting login with {}:{}...'.format(username, password), file=logs)
    element_send_keys(browser, logs, DEFAULT_SLEEP, By.NAME, 'email', username)
    element_send_keys(browser, logs, DEFAULT_SLEEP, By.NAME, 'password', password)
    element_click(browser, logs, DEFAULT_SLEEP, By.XPATH, '//*[@id="root"]/div[1]/div[4]/div[2]/div/div[2]/form/button')
    print(date(), 'Finished login', file=logs)
    wait_until_with_exception(browser, logs, DEFAULT_TIMEOUT, EC.title_is('OPN Platform'))


def sign_out(browser, logs):
    # function for signing out from opnplatform, but it doesn't stop testing
    element_click(browser, logs, DEFAULT_SLEEP, By.XPATH, '//div[@class="login-btn-wrapper"]')
    print(date(), 'Signed out', file=logs)



def random_string_generator(length):
    name = ''
    for i in range(length):
        name += random.choice(string.ascii_uppercase + string.ascii_lowercase)
    return name


def tear_down(browser, logs):
    print(date(), "Congratulations, test finished successfully!", file=logs)
    all_handles = browser.window_handles
    for handle in all_handles:
        browser.switch_to.window(handle)
        browser.close()
    logs.close()


def check_exists_by(browser, by, value):
    try:
        browser.find_element(by, value)
    except NoSuchElementException:
        return False
    return True


def find_element_by_text(browser, text):
    waitForElementWithException(browser, 10, By.XPATH, "//*[contains(text(), '%s')]" % text)
    try:
        element = browser.find_element_by_xpath("//*[contains(text(), '%s')]" % text)
        print(date(), "Element '%s' was found" % text)
    except:
        print(date(), 'Element "%s" is not found' % text)
    return element


def find_elements_by_text(browser, text):

    waitForElementWithException(browser, 10, By.XPATH, "//*[contains(text(), '%s')]" % text)

    element = []

    for elm in browser.find_elements_by_xpath("//*[contains(text(), '%s')]" % text):
        print(date(), elm.text)
        if elm.text != "" or elm.text == None:
            element.append(elm)

    print(date(), "List with elements with length %d is returned" % len(element))
    return element


def waitForElementWithException(browser, time_limit, by, value):

    try:
        element = WebDriverWait(browser, time_limit).until(
            EC.presence_of_element_located((by, value))
        )

    finally:
        print(date(), "Element '%s' was waited" % value)


def clickElementByCoordinate(browser, element, xoffset, yoffset):
    action = ActionChains(browser)
    action.move_to_element_with_offset(element, xoffset, yoffset)
    action.click()
    location = element.location
    location['x'] = location['x'] + xoffset
    location['y'] = location['y'] + yoffset
    print(date(), "Element %s with location %s is clicked" % (element.text, location))
    action.perform()


def show_elements_text(elements_list):
    for elm in elements_list:
        print(date(), elm.text)


def write_error(logs, comment, exception):
    print(date(), comment + ":", file=logs)
    print(date(), sys.exc_info()[0], file=logs)


def date():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S -")



def result_of_the_test(results):
    with open('result.txt', "w") as file_result:
        for line in results:
            file_result.write('%s\n'%line)
