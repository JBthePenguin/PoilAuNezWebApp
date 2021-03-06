from poilaunezdjango.browser_selenium import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BrowseBaseTests(Browser):
    """ Tests for the browsing"""

    def test_navbar(self):
        """ test for nav bar"""
        self.selenium.get(self.live_server_url)
        # title
        page_title = self.selenium.title
        self.assertEqual(page_title, "Poil au nez")
        # logo
        logo_title = self.selenium.find_elements_by_css_selector(
            ".navbar-brand"
        )
        self.assertIn(
            ("Compagnie Poil au Nez" and "Compagnie de clown-théâtre"),
            logo_title[0].text
        )
        # nav links
        nav_links = self.selenium.find_elements_by_css_selector(
            ".nav-link"
        )
        self.assertEqual(len(nav_links), 6)

        def click_on_link(links, link_text, header_text):
            """click on a link and wait it """
            for link in links:
                if link.text == link_text:
                    select_link = link
            select_link.click()
            wait = WebDriverWait(self.selenium, 10)
            wait.until(
                EC.presence_of_element_located(
                    (By.ID, "".join(["header_", header_text]))
                )
            )

        def link_color(links, ind_link):
            """ assert active link color """
            other_links = []
            for x in range(6):
                if x == ind_link:
                    pass
                else:
                    other_links.append(x)
            self.assertNotEqual(
                links[other_links[0]].value_of_css_property("color"),
                links[ind_link].value_of_css_property("color")
            )
            self.assertEqual(
                links[other_links[0]].value_of_css_property("color"),
                links[other_links[1]].value_of_css_property("color"),
                links[other_links[2]].value_of_css_property("color")
            )
            self.assertEqual(
                links[other_links[0]].value_of_css_property("color"),
                links[other_links[3]].value_of_css_property("color"),
                links[other_links[4]].value_of_css_property("color")
            )

        # link Actus
        click_on_link(nav_links, "Actus", "actus")
        self.assertIn(
            ("/actus/"),
            self.selenium.current_url
        )
        nav_links = self.selenium.find_elements_by_css_selector(
            ".nav-link"
        )
        link_color(nav_links, 1)
        # link Galerie
        click_on_link(nav_links, "Galerie", "galery")
        self.assertIn(
            ("/galery/"),
            self.selenium.current_url
        )
        nav_links = self.selenium.find_elements_by_css_selector(
            ".nav-link"
        )
        link_color(nav_links, 2)
        # link Contact
        click_on_link(nav_links, "Contactez-nous", "contact")
        self.assertIn(
            ("/contact/"),
            self.selenium.current_url
        )
        nav_links = self.selenium.find_elements_by_css_selector(
            ".nav-link"
        )
        link_color(nav_links, 5)
        # Dropdown menu
        # link Photos
        hover = ActionChains(self.selenium).move_to_element(nav_links[2])
        hover.perform()
        wait = WebDriverWait(self.selenium, 20)
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "dropdown-item")
            )
        )
        click_on_link(nav_links, "Photos", "photos")
        self.assertIn(
            ("/galery/photos/"),
            self.selenium.current_url
        )
        nav_links = self.selenium.find_elements_by_css_selector(
            ".nav-link"
        )
        link_color(nav_links, 3)
        # link Videos
        hover = ActionChains(self.selenium).move_to_element(nav_links[2])
        hover.perform()
        wait = WebDriverWait(self.selenium, 20)
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "dropdown-item")
            )
        )
        click_on_link(nav_links, "Vidéos", "videos")
        self.assertIn(
            ("/galery/videos/"),
            self.selenium.current_url
        )
        nav_links = self.selenium.find_elements_by_css_selector(
            ".nav-link"
        )
        link_color(nav_links, 4)

    def test_footer(self):
        """ test for footer"""
        self.selenium.get(self.live_server_url)
        divs = self.selenium.find_elements_by_css_selector(
            ".page-footer .row div"
        )
        self.assertEqual(len(divs), 6)


class BrowseIndexTests(Browser):
    """ Tests for the browsing"""

    def test_index(self):
        """ test for index page"""
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # header
        header_title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual(header_title.text, "Qui sommes-nous?")
        images = self.selenium.find_elements_by_css_selector(
            "#header_index .container .row .card"
        )
        self.assertEqual(len(images), 2)
        # main
        divs = self.selenium.find_elements_by_css_selector(
            "#main_index .row div.mx-auto"
        )
        self.assertEqual(len(divs), 5)
        card_titles = self.selenium.find_elements_by_css_selector(
            "#main_index .card .card-body .card-title"
        )
        self.assertEqual(card_titles[1].text, "A la poursuite d'une histoire")
