
from WebAutomation.Src.TestBase.EnvironmentSetUp import EnvironmentSetup
from WebAutomation.Src.PageObject.Pages.Elements import Element
from WebAutomation.Test.TestUtility.ScreenShot import SS
import unittest

class HomePage(EnvironmentSetup):

    def test_Home_Page(self):

# Screenshots relative paths
        ss_path = "/HomePage_screen/"

# Using the driver instances created in EnvironmentSetup
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_page_load_timeout(20)

# Creating object of SS screenshots utility
        ss = SS(driver)
        expected_title = "Swag Labs"
# Validating Page title with the expected one through catching exception
        try:
            if driver.title == expected_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title,expected_title)
        except Exception as e:
            print(e+"WebPage Failed to load")


        inputElement = Element(driver)
        inputElement.setUserName("standard_user")

if __name__ == '__main__':
    unittest.main()
