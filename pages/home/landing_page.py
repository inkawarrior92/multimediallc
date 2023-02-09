from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from random import randrange


class LandingPage(SeleniumDriver):
    log = cl.customLogger((logging.DEBUG))

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _terms_pop_up = "//strong[text()='YOU MUST BE OVER 18 AND AGREE TO THE TERMS BELOW BEFORE CONTINUING:']"
    _i_agree_btn = "//a[text()='I AGREE']"
    _room_lists = "//ul[@id='room_list']/li"

    def clickIagreeButton(self):
        self.waitForElement(self._terms_pop_up, "xpath")
        self.elementClick(self._i_agree_btn, "xpath")

    def verifyTitle(self):
        if "Chaturbate - Free Adult Webcams, Live Sex, Free Sex Chat, Exhibitionist & Pornstar Free Cams" in self.getTitle():
            return True
        else:
            return False

    def click_random_room(self):
        data_list = self.getElementList(self._room_lists, "xpath")
        random_room_num = randrange(1, len(data_list))
        random_room_xpath = self._room_lists + f'[{random_room_num}]/a'
        link = self.getAttribute(locator=random_room_xpath, locatorType='xpath', attribute="href")
        self.elementClick(random_room_xpath, "xpath")
        return link
