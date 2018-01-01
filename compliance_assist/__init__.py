from selenium import webdriver
from compliance_assist.locators import LoginPageLocators
import os


# Import credentials, if available
try:
    from compliance_assist.sensitive import USER_NAME, PASSWORD
except:
    # If sensisitve.py is not available
    USER_NAME = ""
    PASSWORD = ""

DOWNLOAD_DEST = "/Users/mattlewis/Development/python/ComplianceAssist/compliance_assist/data/tmp"

class Site(object):
    
    def __init__(self,download_destination=DOWNLOAD_DEST):

        options = webdriver.ChromeOptions()
        profile = {"plugins.plugins_list": 
                [
                    {"enabled":False,"name":"Chrome PDF Viewer"}
                ],
                "download.default_directory" : download_destination}
        options.add_experimental_option("prefs",profile)
        self.driver = webdriver.Chrome(options = options)
        self.driver.get("https://sanjac.compliance-assist.com/")
        self._login()
    
    def _login(self):
        """
        Login to the Compliance Assist site using credentials imported from
        sensitive module (which is .gitignored).
        """
        # Fetch login fields and submit button
        username_field = self.driver.find_element(
            *LoginPageLocators.USER_NAME_LOCATOR)
        password_field = self.driver.find_element(
            *LoginPageLocators.PASSWORD_LOCATOR)
        submit_button = self.driver.find_element(
            *LoginPageLocators.SUBMIT_LOCATOR)
        # Send username and password to fields
        username_field.send_keys(USER_NAME)
        password_field.send_keys(PASSWORD)
        # Click
        submit_button.click()

    def goto(self,url):
        """
        Navigate to url.
        
        Note: this can be used to download files.
        """
        self.driver.get(url)

    def download(self, url):
        """
        Method to download files at supplied `url` from Compliance Assist and
        save file in local `destination`. 
        
        Note: this method utilizes chromes automatic downloading for files. 
        If the url points to a page chrome wants to load, it will load it.
        """
        download_error_indicator = None
        before = os.listdir(DOWNLOAD_DEST)
        self.goto(url)
        after = os.listdir(DOWNLOAD_DEST)
        change = set(after) - set(before)
        try:
            file_name = change.pop()
        except:
            print("First catch!")
            raise IOError

        # Detects that file could not be found and throws and IOError
        try:
            download_error_indicator = self.driver.find_element(*LoginPageLocators.NO_FILE_FOUND)
        except:
            pass
        if(download_error_indicator):
            print("Second catch!")
            raise IOError   
        


    def _find_element(self,LOCATOR):
        """
        Exposes driver for the purpose of locating elements on site.
        """
        return self.driver.find_element(*LOCATOR)

    def close(self):
        self.driver.close()