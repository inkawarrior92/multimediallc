import time
from pages.home.landing_page import LandingPage
from pages.room.random_room import Room
import unittest
import pytest
# py.test -s -v tests/room/random_room_test.py


@pytest.mark.usefixtures("oneTimeSetUp")
class RoomTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LandingPage(self.driver)
        self.room = Room(self.driver)

    @pytest.mark.run(order=1)
    def test_url(self):
        title = self.lp.click_random_room()
        assert title == self.room.verifyURL()

    @pytest.mark.run(order=2)
    def test_sign_up_btn(self):
        result = self.room.check_sign_up_btn()
        assert result

    @pytest.mark.run(order=3)
    def test_scan_cams(self):
        result = self.room.check_scan_cams()
        assert result

    @pytest.mark.run(order=4)
    def test_send_tip(self):
        result = self.room.check_send_tip()
        assert result

    @pytest.mark.run(order=4)
    def test_video_stream(self):
        result = self.room.check_video_stream_playing()
        assert result

    @pytest.mark.run(order=5)
    def test_scan_cams_clicks(self):
        result = self.room.click_scan_cams()
        assert result
