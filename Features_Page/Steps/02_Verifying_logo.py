import time

from behave import *
from datetime import datetime

@then('Verify that the logo present on page')
def check_logo(context):
    logo_text=context.driver.find_element_by_xpath("//div[@class='orangehrm-login-logo']//img[@alt='orangehrm-logo']").is_displayed()
    print("Logo is present",logo_text)
    dt = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    context.driver.save_screenshot(f"C:\\Users\\Sangram\\PycharmProjects\\BDD_Framework\\Features_Page\\Screenshots\\picture2{dt}.png")
    assert logo_text is True
@then('close browser')
def close_brows(context):
    context.driver.close()
    time.sleep(5)