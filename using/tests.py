from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.filter(password__startswith='bcrypt$$')


class BrowseProductTests(StaticLiveServerTestCase):
    """ Tests browsing inside product app """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_index(self):
        """ tests for navigation in product """
        # index template: -page and header title  -number of sections
        self.selenium.get(self.live_server_url)
        page_title = self.selenium.title
        assert page_title == "Poil au nez"
