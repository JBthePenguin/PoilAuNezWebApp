from poilaunezdjango.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowsePhotoTests(Browser):
    """ Tests for the browsing"""

    def test_photos(self):
        """ test for photos page"""
        self.selenium.get('%s%s' % (self.live_server_url, '/galery/photos/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Photos")
        photos = self.selenium.find_elements_by_css_selector(
            "#header_photos  .carousel-item"
        )
        self.assertEqual(len(photos), 6)
        # main part and display
        photos_titles = self.selenium.find_elements_by_css_selector(
            "#main_photos  .card-body h6"
        )
        self.assertEqual(photos_titles[0].text, "Festiviel 2018 Test")
        # pagination
        self.assertEqual(len(photos_titles), 6)
        next_button = self.selenium.find_element_by_partial_link_text(
            "Suivant")
        next_button.click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[@src='/uploads/test/pag/test.png']"
                )
            )
        )
        photos_cards = self.selenium.find_elements_by_css_selector(
            "#main_photos .card"
        )
        self.assertEqual(len(photos_cards), 4)
