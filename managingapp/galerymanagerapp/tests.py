from poilaunezdjango.browser_selenium import Browser
from managingapp.tests import login, logout
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ManageGaleryTests(Browser):
    """ Tests for manage Actu, add update delete"""

    def test_manage_galery(self):
        """ test for manager galery page"""
        login(self)
        # header
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/manager/galery/'))
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Administration de la galerie")
        # link for visit the galery page on the site
        self.selenium.find_element_by_link_text(
            "Visualiser la galerie sur le site").click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.number_of_windows_to_be(2))
        default_handle = self.selenium.current_window_handle
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Galerie")
        self.selenium.close()
        self.selenium.switch_to_window(default_handle)
        # link for admin photo
        self.selenium.find_element_by_link_text(
            "Adminstration des photos").click()
        wait.until(EC.presence_of_element_located(
            (By.ID, "header_manager_photos")))
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Administration des photos")
        # link for admin video
        self.selenium.back()
        wait.until(EC.presence_of_element_located(
            (By.ID, "header_manager_galery")))
        self.selenium.find_element_by_link_text(
            "Adminstration des vidéos").click()
        wait.until(EC.presence_of_element_located(
            (By.ID, "header_manager_videos")))
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Administration des vidéos")
        logout(self)
