from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class Browser(StaticLiveServerTestCase):
    """ Tests for the browsing"""
    fixtures = [
        'actu_fixtures.json',
        'photo_fixtures.json',
        'video_fixtures.json',
        'manager_fixtures.json',
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
