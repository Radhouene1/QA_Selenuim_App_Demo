from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    # Locators
    _login_link = "//div[@class='p-gridcol col-auto-device-none']//a[text()='Sign In']"
    _email_field = "ctl00_siteContent_txtEmail"
    _password_field = "ctl00_siteContent_txtPassword"
    _login_button = "ctl00_siteContent_btnSignIn"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)


    def login(self, email="", password="", Back=False):
        if Back is True:
            self.driverBack()
        self.screenShot("home_page")
        self.waitForElement(locator=self._login_link,locatorType="xpath", pollFrequency=1)
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.screenShot("login credentials")
        self.clickLoginButton()


    def verifyLoginTitle(self,title):
        return self.verifyPageTitle(title)


    def verifyLoginSuccessful(self):
        self.waitForElement("//div[@class='p-gridcol col-auto-device-none']//a[text()='Sign Out']", locatorType="xpath")
        result = self.isElementPresent(locator="//div[@class='p-gridcol col-auto-device-none']//a[text()='Sign Out']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementDisplayed(locator="//span[contains(text(),'Email Address and Password do not match')]", locatorType="xpath")
        return result

    def logout (self):
        self.elementClick(locator="//div[@class='p-gridcol col-auto-device-none']//a[text()='Sign Out']", locatorType="xpath")

    def clearFields(self):
        self.clearField(locator=self._email_field)
        self.clearField(locator=self._password_field)
