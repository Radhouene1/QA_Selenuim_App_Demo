from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time

class ApplyPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    # Locators
    _job_title ="keywordSearchDsk"
    _search_button = "//span[contains(text(),'Search')]//parent::button"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterJobTitle(self,job):
        self.sendKeys(job, self._job_title)

    def clickSearch(self):
        self.elementClick(self._search_button, locatorType="xpath")

    def searchJob(self,job):
        self.enterJobTitle(job)
        self.clickSearch()

    def verifyJobSearchSuccessful(self,job):
        self.waitForElement("//p[contains(text(),'{}')]//parent::a".format(job), locatorType="xpath")
        self.webScroll("down")
        self.util.sleep(2)
        result = self.isElementPresent(locator="//p[contains(text(),'{}')]//parent::a".format(job), locatorType="xpath")
        self.screenShot("verifyJobSearchSuccessful")
        return result


    def verifyAppSubmitted(self,job):
        self.elementClick("//p[contains(text(),'{}')]".format(job), locatorType="xpath")
        self.util.sleep(2)
        result = self.isElementPresent(locator="//span[contains(text(),'Application Submitted')]//parent::button[@data-tag='applyNowBtn']", locatorType="xpath")
        self.screenShot("verifyAppSubmitted")
        return result
