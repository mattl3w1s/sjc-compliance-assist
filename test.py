import unittest
from selenium import webdriver
from compliance_assist.sensitive import USER_NAME, PASSWORD
from compliance_assist.locators import LoginPageLocators
from compliance_assist import Site

class ComplianceAssistLogin(unittest.TestCase):
    """A simple test to verify that I can login to Compliance Assist."""

    def setUp(self):
        self.site = Site()
    
    def test_login(self):
        """
        Tests login functionality to Compliance Assist site.
        """
        self.site.login()

        # Test
        try:
            self.site.find_element(LoginPageLocators.CONFIRMATION_LOCATOR)
        except:
            assert False

    def tearDown(self):
        self.site.close()

if __name__ == "__main__":
    unittest.main()

