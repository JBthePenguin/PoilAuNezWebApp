from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowseGaleryTests(StaticLiveServerTestCase):
    """ Tests for the browsing"""
    fixtures = ['photo_fixtures.json', 'video_fixtures.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_galery(self):
        """ test for galery page"""
        self.selenium.get('%s%s' % (self.live_server_url, '/galery/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Galerie")
        card_titles = self.selenium.find_elements_by_css_selector(
            "#header_galery  .card-title"
        )
        last_media_titles = self.selenium.find_elements_by_css_selector(
            "#header_galery p"
        )
        self.assertEqual(card_titles[0].text, "... les photos:")
        self.assertEqual(last_media_titles[1].text, "Festiviel 2018 Test")
        self.assertEqual(card_titles[1].text, "... les vidéos:")
        self.assertEqual(last_media_titles[2].text, "Video Test")
        # main
        # photos
        photos = self.selenium.find_elements_by_css_selector(
            "#main_galery  .carousel-item img"
        )
        self.assertEqual(len(photos), 10)
        # videos
        videos = self.selenium.find_elements_by_css_selector(
            "#main_galery  .carousel-item video"
        )
        self.assertEqual(len(videos), 6)
        # links
        photo_link = self.selenium.find_element_by_link_text(
            "Visiter la galerie PHOTOS"
        )
        photo_link.click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "header_photos")
            )
        )
        self.assertIn(
            ("/galery/photos"),
            self.selenium.current_url
        )
        self.selenium.get('%s%s' % (self.live_server_url, '/galery/'))
        video_link = self.selenium.find_element_by_link_text(
            "Visiter la galerie VIDEOS"
        )
        video_link.click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "header_videos")
            )
        )
        self.assertIn(
            ("/galery/videos"),
            self.selenium.current_url
        )
