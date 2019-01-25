from poilaunezdjango.browser_selenium import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from managingapp.tests import login, logout
from poilaunezdjango.settings import MEDIA_ROOT
import time


class ManageActuTests(Browser):
    """ Tests for manage Actu, add update delete"""

    def test_manage_actus(self):
        """ test for manager actus page"""
        login(self)
        self.selenium.get('%s%s' % (self.live_server_url, '/manager/actus/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Administration des actus")
        cards = self.selenium.find_elements_by_class_name('card')
        self.assertEqual(len(cards), 3)
        # link for visit the actus page on the site
        self.selenium.find_element_by_link_text(
            "Visualiser les actualités sur le site").click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.number_of_windows_to_be(2))
        default_handle = self.selenium.current_window_handle
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Actualités")
        self.selenium.close()
        self.selenium.switch_to_window(default_handle)
        # add actu with form
        self.selenium.find_element_by_link_text(
            'Ajouter une actualité').click()
        self.selenium.find_element_by_id("id_image").send_keys(
            "".join([MEDIA_ROOT, "/tests/actus/photo1.jpg"]))
        self.selenium.find_element_by_id("id_title").send_keys(
            "test manage add title")
        self.selenium.find_element_by_id("id_text").send_keys(
            "test manage add text")
        self.selenium.find_element_by_id('btn-form-add-mod').click()
        card_titles = self.selenium.find_elements_by_class_name('card-title')
        self.assertEqual("test manage add title", card_titles[0].text)
        # update actu with form
        update_links = self.selenium.find_elements_by_link_text("Modifier")
        update_links[1].click()
        title = self.selenium.find_element_by_id("id_title").text
        text = self.selenium.find_element_by_id("id_text").text
        self.selenium.find_element_by_id("id_title").clear()
        self.selenium.find_element_by_id("id_title").send_keys(
            "test manage update title")
        self.selenium.find_element_by_id('btn-form-add-mod').click()
        card_titles = self.selenium.find_elements_by_class_name('card-title')
        card_texts = self.selenium.find_elements_by_class_name('card-text')
        self.assertEqual("test manage update title", card_titles[0].text)
        self.assertNotEqual(title, card_titles[0].text)
        self.assertEqual(text, card_texts[1].text)
        # delete actu
        self.assertEqual("test manage add title", card_titles[1].text)
        delete_links = self.selenium.find_elements_by_link_text("Supprimer")
        delete_links[1].click()
        alert = self.selenium.switch_to_alert()
        alert.accept()
        wait.until(EC.alert_is_present())
        alert = self.selenium.switch_to_alert()
        alert.accept()
        time.sleep(2)
        card_titles = self.selenium.find_elements_by_class_name('card-title')
        card_titles_list = []
        for card_title in card_titles:
            card_titles_list.append(card_title.text)
        self.assertNotIn("test manage add title", card_titles_list)
        logout(self)
