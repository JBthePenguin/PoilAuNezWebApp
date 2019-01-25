from poilaunezdjango.browser_selenium import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from managingapp.tests import login, logout
from poilaunezdjango.settings import MEDIA_ROOT
import time


class ManagePhotoTests(Browser):
    """ Tests for manage Photo, add update delete"""

    def test_manage_photos(self):
        """ test for manager photos page"""
        login(self)
        self.selenium.get('%s%s' % (
            self.live_server_url, '/manager/galery/photos/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Administration des photos")
        cards = self.selenium.find_elements_by_class_name('card')
        self.assertEqual(len(cards), 4)
        # link for visit the photos page on the site
        self.selenium.find_element_by_link_text(
            "Visualiser les photos sur le site").click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.number_of_windows_to_be(2))
        default_handle = self.selenium.current_window_handle
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Photos")
        self.selenium.close()
        self.selenium.switch_to_window(default_handle)
        # add actu with form
        self.selenium.find_element_by_link_text(
            'Ajouter une photo').click()
        self.selenium.find_element_by_id("id_image").send_keys(
            "".join([MEDIA_ROOT, "/tests/photos/photo1.jpg"]))
        self.selenium.find_element_by_id("id_title").send_keys(
            "test manage add title")
        self.selenium.find_element_by_id('btn-form-add-mod').click()
        card_titles = self.selenium.find_elements_by_tag_name("h6")
        self.assertEqual("test manage add title", card_titles[0].text)
        # update actu with form
        update_links = self.selenium.find_elements_by_link_text(
            "Modifier le titre")
        update_links[1].click()
        self.selenium.find_element_by_id("id_title").clear()
        self.selenium.find_element_by_id("id_title").send_keys(
            "test manage update title")
        self.selenium.find_element_by_id('btn-form-add-mod').click()
        card_titles = self.selenium.find_elements_by_tag_name("h6")
        self.assertEqual("test manage update title", card_titles[0].text)
        # delete actu
        self.assertEqual("test manage add title", card_titles[1].text)
        delete_links = self.selenium.find_elements_by_link_text("Supprimer")
        delete_links[1].click()
        alert = self.selenium.switch_to_alert()
        alert.accept()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.alert_is_present())
        alert = self.selenium.switch_to_alert()
        alert.accept()
        time.sleep(2)
        card_titles = self.selenium.find_elements_by_tag_name("h6")
        card_title_texts = []
        for card_title in card_titles:
            card_title_texts.append(card_title.text)
        self.assertNotIn("test manage add title", card_title_texts)
        logout(self)
