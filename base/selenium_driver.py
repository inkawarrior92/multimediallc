from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


# anything selenium driver, will be written here.
class SeleniumDriver:

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Elements Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Elements not found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    # Either provide element or a combinator of locator and locatorType
    def elementClick(self, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    # Either provide element or a combinator of locator and locatorType
    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def getAttribute(self,  locator="", locatorType="id", attribute="", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            attr_value = element.get_attribute(attribute)
            if len(attr_value) == 0:
                attr_value = element.get_attribute("innerText")
            if len(attr_value) != 0:
                attr_value = attr_value.strip()
        except:
            self.log.error(f"Failed to get text attribute for {attribute}")
            print_stack()
            attr_value = None
        return attr_value

    def isElementPresent(self, locator, locatorType="id", element=None):
        """
            Check if element is present
            Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.driver.find_element(locatorType, locator)
            if element is not None:
                self.log.info("Element Found with locator: " + locator + " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            self.log.info("Element not found with locator: " + locator + " locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " locatoryType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator + " locatorType " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for a maximum of " + str(timeout) + "seconds for element " + str(locator)
                          + "to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element appeared on the webpage")

        except:
            self.log.info(f"Element {locator} does not appear on the web page")
            print_stack()
        return element

    def getTitle(self):
        self.log.info("Title Caputured: " + self.driver.title)
        return self.driver.title

    def getURL(self):
        self.log.info("URL Captured: " + self.driver.current_url)
        return self.driver.current_url





