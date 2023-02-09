import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Room(SeleniumDriver):
    log = cl.customLogger((logging.DEBUG))

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _i_agree_btn = "//a[text()='I AGREE']"
    _sign_up_btn = "//ul[@id='nav']/a"
    _cams_link = "//span[contains(text(),'CAM')]"
    _send_tip = "//div[@data-paction='CurrentShowBuyBox']/div/span"
    _active_stream = "//div[contains(@class,'vjs-playing')]"

    def verifyURL(self):
        return self.getURL()

    def check_sign_up_btn(self):
        self.waitForElement(self._sign_up_btn, "xpath")
        result = self.isElementDisplayed(self._sign_up_btn, "xpath")
        return result

    def check_scan_cams(self):
        self.waitForElement(self._cams_link, "xpath")
        result = self.isElementDisplayed(self._cams_link, "xpath")
        return result

    def check_send_tip(self):
        self.waitForElement(self._send_tip, "xpath")
        result = self.isElementDisplayed(self._send_tip, "xpath")
        return result

    def check_video_stream_playing(self):
        self.waitForElement(self._active_stream, "xpath")
        result = self.isElementPresent(self._active_stream, "xpath")
        return result

    def click_scan_cams(self):
        self.log.info("Starting Click scan cams function")
        url_lst = []
        url = self.getURL()
        url_lst.append(url)
        for x in range(3):
            while url in url_lst:
                self.waitForElement(self._cams_link, "xpath")
                self.elementClick(self._cams_link, "xpath")
                time.sleep(2)
                url = self.getURL()
            url_lst.append(url)

        # print(url_lst)
        if len(url_lst) == len(set(url_lst)):
            return True
        else:
            return False



