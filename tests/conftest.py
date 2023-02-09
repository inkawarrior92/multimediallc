import pytest
import os
from base.webdriver_factory import WebDriverFactory
from pages.home.landing_page import LandingPage
from configparser import ConfigParser
import time
@pytest.fixture()
def setUp():
    print("Running Method Level SetUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope='class')
def oneTimeSetUp(request, browser):
    print("\nRunning one time set up")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LandingPage(driver)
    lp.clickIagreeButton()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("\nRunning one time tearDown")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    # can add other options here
    # parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

