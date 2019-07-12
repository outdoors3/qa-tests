# import qalib
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# name_of_test = "T-001-002"
#
# description = "login prod testing"
# result = []
# def callback():
#
#     login = 'opntesting3@gmail.com'
#
#     gpassword = 'Secret99'
#     try:
#
#         qalib.WHICH_PLATFORM = ""
#
#         browser, logs = qalib.set_up("chrome", "stdout", "false")
#
#         qalib.load_main_page(browser, logs)
#         result.append("Success")
#     except:
#         result.append("Fail")
#
#     qalib.result_of_the_test(result)
#     qalib.tear_down(browser, logs)
# qalib.register_qa_test(name_of_test, description, callback)
