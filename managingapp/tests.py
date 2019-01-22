from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from captcha.conf import settings


def login(test_class):
    """ function for login at the begining of a class test"""
    test_class.selenium.get('%s%s' % (test_class.live_server_url, '/manager/'))
    # form
    test_class.selenium.find_element_by_id("id_username").send_keys(
        "testmanager")
    test_class.selenium.find_element_by_id("id_password").send_keys(
        "test2test2")
    settings.CAPTCHA_TEST_MODE = True
    test_class.selenium.find_element_by_id("id_captcha_1").send_keys("PASSED")
    test_class.selenium.find_element_by_css_selector(
        '.form-signin button').click()
    wait = WebDriverWait(test_class.selenium, 10)
    wait.until(EC.presence_of_element_located((By.ID, "header_dashboard")))


def logout(class_test):
    """ function for logout at the end of a class test"""
    class_test.selenium.find_element_by_class_name("fa-sign-out").click()
    wait = WebDriverWait(class_test.selenium, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form-signin")))


class ManagerLoginTests(StaticLiveServerTestCase):
    """ Tests for the manager login and logout"""
    fixtures = ["manager_fixtures.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login_logout(self):
        """ test for login form and logout button"""
        # login
        self.selenium.get('%s%s' % (self.live_server_url, '/manager/'))
        divs = self.selenium.find_elements_by_css_selector(
            "#NavBar div"
        )
        self.assertEqual(len(divs), 2)
        login(self)
        divs = self.selenium.find_elements_by_css_selector(
            "#NavBar div"
        )
        self.assertEqual(len(divs), 3)
        # logout
        logout(self)
        divs = self.selenium.find_elements_by_css_selector(
            "#NavBar div"
        )
        self.assertEqual(len(divs), 2)


class BrowseManagerTests(StaticLiveServerTestCase):
    """ Tests for the manager login and logout"""
    fixtures = ["manager_fixtures.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_navbar(self):
        """ test for the navbar manager """
        login(self)
        # Visit site
        self.selenium.find_element_by_link_text(
            "Page d'accueil du site").click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.number_of_windows_to_be(2))
        default_handle = self.selenium.current_window_handle
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Qui sommes-nous?")
        self.selenium.close()
        self.selenium.switch_to_window(default_handle)
        # Dashboard link
        self.selenium.find_element_by_link_text(
            "Adminstration des actualités").click()
        wait.until(EC.presence_of_element_located(
            (By.ID, "header_manager_actus")))
        self.selenium.find_element_by_link_text(
            "Tableau de bord").click()
        wait.until(EC.presence_of_element_located((By.ID, "header_dashboard")))
        window_handlle = self.selenium.current_window_handle
        self.assertEqual(default_handle, window_handlle)
        logout(self)

    def test_dashboard(self):
        """ test for the dasboard links """
        login(self)
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/manager/dashboard/'))
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Tableau de bord")
        # link manager actu
        self.selenium.find_element_by_link_text(
            "Adminstration des actualités").click()
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.presence_of_element_located(
            (By.ID, "header_manager_actus")))
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Administration des actus")
        self.selenium.find_element_by_link_text(
            "Tableau de bord").click()
        wait.until(EC.presence_of_element_located((By.ID, "header_dashboard")))
        # link manager galery
        self.selenium.find_element_by_link_text(
            "Adminstration de la galerie").click()
        wait.until(EC.presence_of_element_located(
            (By.ID, "header_manager_galery")))
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Administration de la galerie")
        self.selenium.find_element_by_link_text(
            "Tableau de bord").click()
        wait.until(EC.presence_of_element_located((By.ID, "header_dashboard")))
        # link manager message
        self.selenium.find_element_by_link_text(
            "Boîte à messages").click()
        wait.until(EC.presence_of_element_located(
            (By.ID, "header_manager_message")))
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Boîte à messages")
        logout(self)
