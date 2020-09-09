"""Contain the functional tests for the User Stories played by members.

The emulated web browser is Chrome.
Here are the User Stories, in French:
US001 - En tant que Laurent, je veux poster un fichier sur la plateforme pour
        transmettre mon certificat médical.
US002 - En tant que Laurent, je veux indiquer mes coordonnées pour être
        joignable par d’autres adhérents.
US003 - En tant que Laurent, je veux renseigner des informations à destination
        des adhérents pour proposer des créneaux d'entraînement.
US004 - En tant que Claire, je veux consulter l'agenda pour connaître les
        événements passés et à venir.
US005 - En tant que Claire, je veux télécharger ou ouvrir un document pour lire
        un compte-rendu de réunion.
US006 - En tant que Pierre, je veux accéder à certaines informations des
        adhérents pour rencontrer d'autres coureurs.
US007 - En tant que Pierre, je veux consulter la liste des articles disponibles
        pour obtenir une tenue de sport.
US008 - En tant que Pierre, je veux renseigner une pré-commande pour obtenir
        une tenue de sport.
US009 - En tant que Pierre, je veux connaître les adhérents intéressés par une
        pratique en groupe pour s'entraîner ensemble.
"""

# import re

# from django.contrib.sites.models import Site
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumlogin import force_login
from webdriver_manager.chrome import ChromeDriverManager

from teamspirit.core.models import Address
from teamspirit.profiles.models import Personal
from teamspirit.users.models import User


class NoStaffUserStoriesAuthenticatedTestCase(StaticLiveServerTestCase):
    """Contain the functional tests with authenticated user."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # initialize a webdriver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=chrome_options
        )
        # set home_url
        cls.home_url = f"{cls.live_server_url}/"

    def setUp(self):
        super().setUp()
        # a user in database
        self.address = Address.objects.create(
            label_first="1 rue de l'impasse",
            label_second="",
            postal_code="75000",
            city="Paris",
            country="France"
        )
        self.personal = Personal.objects.create(
            phone_number="01 02 03 04 05",
            address=self.address
        )
        self.user = User.objects.create_user(
            email="toto@mail.com",
            first_name="Toto",
            last_name="LE RIGOLO",
            password="TopSecret",
            personal=self.personal
        )
        # force login for this user
        force_login(self.user, self.driver, self.live_server_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_update_last_name_and_first_name(self):
        """US002-AT01: successful update of last name and first name."""
        # ask for the profile page
        start_url = self.home_url + "profile/"
        self.driver.get(start_url)
        # click on the tab "Etat civil"
        names_tab = self.driver.find_element_by_id("etat-civil")
        names_tab.click()
        # click on the button "Modifier"
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.element_to_be_clickable((
            By.ID,
            "change_names_button"
        ))).click()
        # wait for page loading
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.url_changes(start_url))
        # check wether the page is reachable
        expected_url = start_url + "update_personal_info/?"
        self.assertEqual(self.driver.current_url, expected_url)
        # update data
        last_name_field = self.driver.find_element_by_id("id_last_name")
        last_name_field.clear()
        last_name_field.send_keys("le rikiki")
        first_name_field = self.driver.find_element_by_id("id_first_name")
        first_name_field.clear()
        first_name_field.send_keys("titi")
        # click on the button "Mettre à jour"
        submit_button = self.driver.find_element_by_id("submit-id-submit")
        submit_button.click()
        # wait for page loading
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.url_changes(expected_url))
        # check wether the page is reachable
        self.assertEqual(self.driver.current_url, start_url)
        # check wether data are updated
        names_tab = self.driver.find_element_by_id("etat-civil")
        names_tab.click()
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.element_to_be_clickable((
            By.ID,
            "change_names_button"
        )))
        last_name_field = self.driver.find_element_by_id("last_name_field")
        last_name_value = last_name_field.get_attribute("value")
        self.assertEqual(last_name_value, "LE RIKIKI")
        first_name_field = self.driver.find_element_by_id("first_name_field")
        first_name_value = first_name_field.get_attribute("value")
        self.assertEqual(first_name_value, "Titi")

    def test_update_phone_and_address_name(self):
        """US002-AT02: successful update of phone number and address."""
        # ask for the profile page
        start_url = self.home_url + "profile/"
        self.driver.get(start_url)
        # click on the tab "Coordonnées"
        contact_info_tab = self.driver.find_element_by_id("coordonnees")
        contact_info_tab.click()
        # click on the button "Modifier"
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.element_to_be_clickable((
            By.ID,
            "update_phone_address"
        ))).click()
        # wait for page loading
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.url_changes(start_url))
        # check wether the page is reachable
        expected_url = start_url + "update_phone_address/?"
        self.assertEqual(self.driver.current_url, expected_url)
        # update data
        phone_field = self.driver.find_element_by_id("id_phone_number")
        phone_field.clear()
        phone_field.send_keys("99 98 97 96 95")
        label_first_field = self.driver.find_element_by_id("id_label_first")
        label_first_field.clear()
        label_first_field.send_keys("12 rue du Pont")
        label_second_field = self.driver.find_element_by_id("id_label_second")
        label_second_field.clear()
        label_second_field.send_keys("Appartement 3")
        postal_code_field = self.driver.find_element_by_id("id_postal_code")
        postal_code_field.clear()
        postal_code_field.send_keys("79000")
        city_field = self.driver.find_element_by_id("id_city")
        city_field.clear()
        city_field.send_keys("Niort")
        country_field = self.driver.find_element_by_id("id_country")
        country_field.clear()
        country_field.send_keys("Suisse")
        confidentiality_checkbox_label = self.driver.find_element_by_xpath(
            "//label[@for='id_has_private_profile']"
        )
        confidentiality_checkbox_label.click()
        # click on the button "Mettre à jour"
        submit_button = self.driver.find_element_by_id(
            "submit-phone-address-form"
        )
        submit_button.click()
        # wait for page loading
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.url_changes(expected_url))
        # check wether the page is reachable
        self.assertEqual(self.driver.current_url, start_url)
        # check wether data are updated
        contact_info_tab = self.driver.find_element_by_id("coordonnees")
        contact_info_tab.click()
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.element_to_be_clickable((
            By.ID,
            "update_phone_address"
        )))
        phone_field = self.driver.find_element_by_id("phone_field")
        phone_value = phone_field.get_attribute("value")
        self.assertEqual(phone_value, "99 98 97 96 95")
        label_first_field = self.driver.find_element_by_id("label_first_field")
        first_name_value = label_first_field.get_attribute("value")
        self.assertEqual(first_name_value, "12 rue du Pont")
        label_second_field = self.driver.find_element_by_id(
            "label_second_field"
        )
        label_second_value = label_second_field.get_attribute("value")
        self.assertEqual(label_second_value, "Appartement 3")
        postal_code_and_city_field = self.driver.find_element_by_id(
            "postal_code_and_city_field"
        )
        postal_code_and_city_value = postal_code_and_city_field.get_attribute(
            "value"
        )
        self.assertEqual(postal_code_and_city_value, "79000 Niort")
        country_field = self.driver.find_element_by_id("country_field")
        country_value = country_field.get_attribute("value")
        self.assertEqual(country_value, "Suisse")
        confidentiality_checkbox = self.driver.find_element_by_id(
            "confidential_checkbox"
        )
        self.assertTrue(confidentiality_checkbox.is_selected())
