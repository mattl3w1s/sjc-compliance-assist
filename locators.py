from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should be
    added here.
    """
    USER_NAME = (By.Name, 'UserName')
    PASSWORD = (By.Name, "Password")
    SUBMIT = (By.Name, "submitButton")