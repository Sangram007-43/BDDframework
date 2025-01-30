from behave import *
from selenium import webdriver
import time
from datetime import datetime

#GlobaL Variables
LOGIN_URL= "https://opensource-demo.orangehrmlive.com/"

@given('Launch Chrome Browser')
def Open_Browser_Login(context):
    context.driver= webdriver.Chrome(executable_path=r"C:\Users\Sangram\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe")
    context.driver.maximize_window()

@when('Open OrangeHRM websites')
def Launching_Website(context):
    context.driver.get(LOGIN_URL)
    time.sleep(5)

@when('Enter User "{Username}" and Password "{Password}"')
def Enter_User_Pwd(context,Username,Password):
    context.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(Username)
    context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(Password)

@then('Click on Login')
def Login_Button(context):
    context.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
    time.sleep(5)
    dt= datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    context.driver.save_screenshot(f"C:\\Users\\Sangram\\PycharmProjects\\BDD_Framework\\Features_Page\\Screenshots\\picture1{dt}.png")
    time.sleep(5)