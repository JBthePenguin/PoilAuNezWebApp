from poilaunezdjango.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowseActuTests(Browser):
    """ Tests for the browsing"""

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
        actu_display_links = self.selenium.find_elements_by_link_text(
            "Afficher"
        )
        actu_display_links[1].click()
        wait = WebDriverWait(self.selenium, 30)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[@class='card-img-top' and @src='test/display/actu1.png']"
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
                    "//img[@class='w-100' and @src='test/pag/actu1.png']"
                )
            )
        )
        actu_cards = self.selenium.find_elements_by_css_selector(
            "#main_actus .card"
        )
        self.assertEqual(len(actu_cards), 2)
