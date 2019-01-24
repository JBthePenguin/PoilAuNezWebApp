from poilaunezdjango.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from captcha.conf import settings


class BrowseContactTests(Browser):
    """ Tests for the browsing"""

    def test_contact(self):
        """ test for contact page"""
        self.selenium.get('%s%s' % (self.live_server_url, '/contact/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Contactez-nous")
        contact_infos = self.selenium.find_elements_by_css_selector(
            "#header_contact li"
        )
        self.assertEqual(len(contact_infos), 4)
        # main send form
        self.selenium.find_element_by_id("id_contact_name").send_keys(
            "testuser")
        self.selenium.find_element_by_id("id_contact_email").send_keys(
            "testuser@email.com")
        self.selenium.find_element_by_id("id_subject").send_keys("test")
        self.selenium.find_element_by_id("id_content").send_keys("text test")
        settings.CAPTCHA_TEST_MODE = True
        self.selenium.find_element_by_id("id_captcha_1").send_keys("PASSED")
        self.selenium.find_element_by_css_selector(
            '#contact-form button').click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.CLASS_NAME,
                    "alert-warning"
                )
            )
        )
        send_msg = self.selenium.find_element_by_class_name("alert-warning")
        self.assertEqual(send_msg.text, "Votre Message a bien été envoyé.")
