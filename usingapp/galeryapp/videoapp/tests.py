from poilaunezdjango.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowseVideoTests(Browser):
    """ Tests for the browsing"""

    def test_videos(self):
        """ test for videos page"""
        self.selenium.get('%s%s' % (self.live_server_url, '/galery/videos/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Vidéos")
        videos = self.selenium.find_elements_by_css_selector(
            "#header_videos  .carousel-item"
        )
        self.assertEqual(len(videos), 4)
        # main part and display
        videos_titles = self.selenium.find_elements_by_css_selector(
            "#main_videos  .card-body h6"
        )
        self.assertEqual(videos_titles[0].text, "Video Test")
        # pagination
        self.assertEqual(len(videos_titles), 4)
        next_button = self.selenium.find_element_by_partial_link_text(
            "Suivant")
        next_button.click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//source[@src='/uploads/test/pag/test.mkv']"
                )
            )
        )
        videos_cards = self.selenium.find_elements_by_css_selector(
            "#main_videos .card"
        )
        self.assertEqual(len(videos_cards), 2)
