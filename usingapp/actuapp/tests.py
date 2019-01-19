from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        last_actu_title = self.selenium.find_element_by_css_selector(
            "#header_actus .card .card-body .card-title"
        )
        self.assertEqual(last_actu_title.text, "actu test 6")
        # main part and display
        actu_display_links = self.selenium.find_elements_by_css_selector(
            "#main_actus .card-text a"
        )
        actu_display_links[1].click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[@class='card-img-top' and @src='/uploads/test/display/actu1.png']"
                )
            )
        )
        display_actu_title = self.selenium.find_element_by_css_selector(
            "#header_actus .card .card-body .card-title"
        )
        self.assertEqual(display_actu_title.text, "actu test 5")
        # pagination
        actu_cards = self.selenium.find_elements_by_css_selector(
            "#main_actus .card"
        )
        self.assertEqual(len(actu_cards), 4)
        next_button = self.selenium.find_element_by_partial_link_text(
            "Suivant")
        next_button.click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[@class='w-100' and @src='/uploads/test/pag/actu1.png']"
                )
            )
        )
        actu_cards = self.selenium.find_elements_by_css_selector(
            "#main_actus .card"
        )
        self.assertEqual(len(actu_cards), 2)
