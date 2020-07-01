"""Contain the functional tests for the general User Stories.

The emulated web browser is Chrome.
Here are the User Stories, in French:
US022 - En tant que Toto, je veux accéder à la page de connexion pour me
        connecter à l'application.
US023 - En tant que Toto, je veux me connecter à l’application.
US024 - En tant que Toto, je veux accéder à la page d'accueil pour naviguer sur
        le site.
US025 - En tant que Toto, je veux accéder à chaque page de l'application pour
        naviguer sur le site.
US026 - En tant que Toto, je veux accéder à la page de contact pour communiquer
        avec le bureau de l'association.
US027 - En tant que Toto, je veux accéder à la page des mentions légales pour
        le plaisir.
US028 - En tant que Toto, je veux modifier mon mot de passe.
US029 - En tant que Toto, je veux réinitialiser mon mot de passe.
US030 - En tant que Toto, je veux me déconnecter de l’application.
"""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import ugettext_lazy as _
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import url_changes
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from teamspirit.users.models import User


class GeneralUserStoriesAnonymousTestCase(StaticLiveServerTestCase):
    """Contain the functional tests with anonymous user."""

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
        cls.driver.maximize_window()
        # set home_url
        cls.home_url = f"{cls.live_server_url}/"

    def setUp(self):
        super().setUp()
        # a user in database
        self.user_a = User.objects.create_user(
            email="toto@mail.com",
            first_name="Toto",
            password="TopSecret"
        )
        self.user_b = User.objects.create_user(
            email="titi@mail.com",
            first_name="Titi",
            password="Grosminet",
            is_active=False
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_login_success(self):
        """US023-TA01: successful login."""
        # start from the login page
        start_url = self.home_url + "users/login/"
        self.driver.get(start_url)
        # fill the login form
        email_field = self.driver.find_element_by_id("id_username")
        email_field.send_keys("toto@mail.com")
        password_field = self.driver.find_element_by_id("id_password")
        password_field.send_keys("TopSecret")
        # click on the button "Se connecter"
        submit_button = self.driver.find_element_by_id("submit-id-submit")
        submit_button.click()
        # wait for page loading
        WebDriverWait(
            self.driver,
            timeout=2
        ).until(url_changes(start_url))
        # redirect to home page: True or False?
        self.assertEqual(self.driver.current_url, self.home_url)
        # user authenticated: True or False?
        custom_welcome = self.driver.find_element_by_id("custom_welcome")
        self.assertEqual(custom_welcome.text, "BIENVENUE TOTO")

    def test_login_failure_wrong_email(self):
        """US023-TA02: login failed with wrong email."""
        # start from the login page
        start_url = self.home_url + "users/login/"
        self.driver.get(start_url)
        # fill the login form
        email_field = self.driver.find_element_by_id("id_username")
        email_field.send_keys("fail@mail.com")
        password_field = self.driver.find_element_by_id("id_password")
        password_field.send_keys("TopSecret")
        # click on the button "Se connecter"
        submit_button = self.driver.find_element_by_id("submit-id-submit")
        submit_button.click()
        # get an error message: True or False?
        error_message = self.driver.find_element_by_xpath(
            "//div[@class='alert alert-block alert-danger']/ul/li"
        )
        message_1 = _(
            "Please enter a correct Email and password. Note that both fields"
            " may be case-sensitive."
        )
        message_2 = "Saisissez un Courriel et un mot de passe valides. "
        "Remarquez que chacun de ces champs est sensible à la casse "
        "(différenciation des majuscules/minuscules)."
        self.assertTrue(
            (error_message.text == message_1) or
            (error_message.text == message_2)
        )
        print(error_message.text)
        print(message_1)
        print(message_2)
        self.assertEqual(error_message.text, message_1)
        self.assertEqual(error_message.text, message_2)
        # stay on current page: True or False?
        self.assertEqual(self.driver.current_url, start_url)

    def test_login_failure_wrong_password(self):
        """US023-TA03: login failed with wrong password."""
        # start from the login page
        start_url = self.home_url + "users/login/"
        self.driver.get(start_url)
        # fill the login form
        email_field = self.driver.find_element_by_id("id_username")
        email_field.send_keys("toto@mail.com")
        password_field = self.driver.find_element_by_id("id_password")
        password_field.send_keys("WrongPassword")
        # click on the button "Se connecter"
        submit_button = self.driver.find_element_by_id("submit-id-submit")
        submit_button.click()
        # get an error message: True or False?
        error_message = self.driver.find_element_by_xpath(
            "//div[@class='alert alert-block alert-danger']/ul/li"
        )
        message_1 = _(
            "Please enter a correct Email and password. Note that both fields"
            " may be case-sensitive."
        )
        message_2 = "Saisissez un Courriel et un mot de passe valides. "
        "Remarquez que chacun de ces champs est sensible à la casse "
        "(différenciation des majuscules/minuscules)."
        self.assertTrue(
            (error_message.text == message_1) or
            (error_message.text == message_2)
        )
        # stay on current page: True or False?
        self.assertEqual(self.driver.current_url, start_url)

    def test_login_failure_inactive_user(self):
        """US023-TA04: login failed with inactive user."""
        # start from the login page
        start_url = self.home_url + "users/login/"
        self.driver.get(start_url)
        # fill the login form
        email_field = self.driver.find_element_by_id("id_username")
        email_field.send_keys("titi@mail.com")
        password_field = self.driver.find_element_by_id("id_password")
        password_field.send_keys("Grosminet")
        # click on the button "Se connecter"
        submit_button = self.driver.find_element_by_id("submit-id-submit")
        submit_button.click()
        # get an error message: True or False?
        error_message = self.driver.find_element_by_xpath(
            "//div[@class='alert alert-block alert-danger']/ul/li"
        )
        message_1 = _(
            "Please enter a correct Email and password. Note that both fields"
            " may be case-sensitive."
        )
        message_2 = "Saisissez un Courriel et un mot de passe valides. "
        "Remarquez que chacun de ces champs est sensible à la casse "
        "(différenciation des majuscules/minuscules)."
        self.assertTrue(
            (error_message.text == message_1) or
            (error_message.text == message_2)
        )
        # stay on current page: True or False?
        self.assertEqual(self.driver.current_url, start_url)
