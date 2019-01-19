from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class BrowseActuTests(StaticLiveServerTestCase):
    """ Tests for the browsing"""
    fixtures = ['actu_fixtures.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_actus(self):
        """ test for actus page"""
        self.selenium.get('%s%s' % (self.live_server_url, '/actus/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Actualités")
