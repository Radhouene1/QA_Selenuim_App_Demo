"""
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

import traceback
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """

        baseURL = "https://neoxam.csod.com/ux/ats/careersite/6/home?c=neoxam&lang=en-US"


        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            """
            Make sure that you downloaded the chrome driver and you exported the PATH
            """
            driver = webdriver.Chrome()
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
