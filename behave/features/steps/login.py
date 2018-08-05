from behave import *
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


TEST_URL = "https://sprinkle-burn.glitch.me/"
EMAIL_LOCATOR = "//input[contains(@type,'email')]"
PASSWORD_LOCATOR = "//input[contains(@type,'password')]"
LOGIN_BUTTON_LOCATOR = "//button[contains(text(),'Login')]"


@given(u'the user has the correct credentials')
def step_impl(context):
    context.browser.get(TEST_URL)
    global user
    global password
    user = "test@drugdev.com"
    password = "supers3cret"


@when(u'the user enters username')
def step_impl(context):
    context.browser.find_element(By.XPATH, EMAIL_LOCATOR).send_keys(user)


@when(u'the user enters password')
def step_impl(context):
    context.browser.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(password)


@when(u'clicks Login')
def step_impl(context):
    context.browser.find_element(By.XPATH, LOGIN_BUTTON_LOCATOR).click()


@then(u'the user is presented with a welcome message')
def step_impl(context):
    wait_until_visible_text(context.browser, "Welcome Dr I Test")
    should_be_equal_as_strings(context.browser, "Welcome Dr I Test")


@given(u'the user has the incorrect credentials')
def step_impl(context):
    context.browser.get(TEST_URL)
    global user
    global password
    user = ""
    password = ""


@then(u'the user is presented with an error message')
def step_impl(context):
    wait_until_visible_text(context.browser, "Credentials are incorrect")
    should_be_equal_as_strings(context.browser, "Credentials are incorrect")


def wait_until_visible_text(driver, text, timeout=2):
    locator = "//*[text()[contains(.,'" + text + "')]]"
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False


def should_be_equal_as_strings(driver, text):
    locator = "//*[text()[contains(.,'" + text + "')]]"
    assert text == driver.find_element(By.XPATH, locator).text