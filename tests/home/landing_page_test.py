from pages.home.landing_page import LandingPage
import unittest
import pytest

# py.test -s -v tests/home/landing_page_test.py --browser chrome/firefox


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        # Make class objects here!
        self.lp = LandingPage(self.driver)

    def test_terms(self):
        assert self.lp.verifyTitle()

