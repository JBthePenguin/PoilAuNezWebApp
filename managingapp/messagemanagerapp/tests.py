from poilaunezdjango.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from managingapp.tests import login, logout
import time


class ManageMessageTests(Browser):
    """ Tests for manage Message, read delete"""

    def test_manage_actus(self):
        """ test for manager messages page"""
        login(self)
        self.selenium.get('%s%s' % (self.live_server_url, '/manager/message/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Boîte à messages")
        messages = self.selenium.find_elements_by_tag_name('tr')
        self.assertEqual((len(messages) - 1), 3)
        # display message in main
        msg_subjects = self.selenium.find_elements_by_css_selector("td a")
        msg_subjects[3].click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.TAG_NAME,
                    "main"
                )
            )
        )
        name = self.selenium.find_element_by_id('contact_name')
        email = self.selenium.find_element_by_id('contact_email')
        date = self.selenium.find_element_by_id('date')
        subject = self.selenium.find_element_by_id('subject')
        content = self.selenium.find_element_by_css_selector('#content p')
        self.assertEqual(name.text, "the boss")
        self.assertEqual(email.text, "theboss@ggg.om")
        self.assertEqual(date.text, "28/01/2019 à 10:58")
        self.assertEqual(subject.text, "Réunion générale")
        self.assertEqual(content.text, "Réunion à 17h")
        # close message
        self.selenium.find_element_by_class_name("btn-dark").click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fa-check")))
        # delete message
        del_links = self.selenium.find_elements_by_class_name('fa-trash-o')
        del_links[2].click()
        wait.until(EC.alert_is_present())
        alert = self.selenium.switch_to_alert()
        alert.accept()
        wait.until(EC.alert_is_present())
        alert = self.selenium.switch_to_alert()
        alert.accept()
        time.sleep(10)
        messages = self.selenium.find_elements_by_tag_name('tr')
        self.assertEqual((len(messages) - 1), 2)
        logout(self)
