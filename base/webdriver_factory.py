from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging
import time


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        logging.getLogger('WDM').setLevel(logging.NOTSET)
        baseURL = "https://chaturbate.com/"
        if self.browser == "firefox":
            s = Service(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=s)
        else:
            s = Service(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        time.sleep(2)
        driver.get(baseURL)
        return driver
