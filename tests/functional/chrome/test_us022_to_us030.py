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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumlogin import force_login
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

    def test_access_login_page(self):
        """US022-AT01: successful access to login page."""
        # ask for the login page
        start_url = self.home_url + "users/login/"
        self.driver.get(start_url)
        # check wether the page is reachable
        self.assertEqual(self.driver.current_url, start_url)

    def test_login_success(self):
        """US023-AT01: successful login."""
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
            timeout=10
        ).until(EC.url_changes(start_url))
        # redirect to home page: True or False?
        self.assertEqual(self.driver.current_url, self.home_url)
        # user authenticated: True or False?
        custom_welcome = self.driver.find_element_by_id("custom_welcome")
        self.assertEqual(custom_welcome.text, "BIENVENUE TOTO")

    def test_login_failure_wrong_email(self):
        """US023-AT02: login failed with wrong email."""
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
        message_1 = "Please enter a correct Email and password. Note that " \
            "both fields may be case-sensitive."
        message_2 = "Saisissez un Courriel et un mot de passe valides. " \
            "Remarquez que chacun de ces champs est sensible à la casse " \
            "(différenciation des majuscules/minuscules)."
        self.assertTrue(
            (error_message.text == message_1) or
            (error_message.text == message_2)
        )
        # stay on current page: True or False?
        self.assertEqual(self.driver.current_url, start_url)

    def test_login_failure_wrong_password(self):
        """US023-AT03: login failed with wrong password."""
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
        message_1 = "Please enter a correct Email and password. Note that " \
            "both fields may be case-sensitive."
        message_2 = "Saisissez un Courriel et un mot de passe valides. " \
            "Remarquez que chacun de ces champs est sensible à la casse " \
            "(différenciation des majuscules/minuscules)."
        self.assertTrue(
            (error_message.text == message_1) or
            (error_message.text == message_2)
        )
        # stay on current page: True or False?
        self.assertEqual(self.driver.current_url, start_url)

    def test_login_failure_inactive_user(self):
        """US023-AT04: login failed with inactive user."""
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
        message_1 = "Please enter a correct Email and password. Note that " \
            "both fields may be case-sensitive."
        message_2 = "Saisissez un Courriel et un mot de passe valides. " \
            "Remarquez que chacun de ces champs est sensible à la casse " \
            "(différenciation des majuscules/minuscules)."
        self.assertTrue(
            (error_message.text == message_1) or
            (error_message.text == message_2)
        )
        # stay on current page: True or False?
        self.assertEqual(self.driver.current_url, start_url)


class GeneralUserStoriesAuthenticatedTestCase(StaticLiveServerTestCase):
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
        self.user = User.objects.create_user(
            email="toto@mail.com",
            first_name="Toto",
            password="TopSecret"
        )
        # force login for this user
        force_login(self.user, self.driver, self.live_server_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_logout(self):
        """US030-AT01: successful logout."""
        # start from the home page
        start_url = self.home_url
        self.driver.get(start_url)
        # click on the link "Déconnexion"
        toggler = self.driver.find_elements_by_class_name('navbar-toggler-icon')[0]
        toggler.click()
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.element_to_be_clickable((By.ID, "logout_link"))).click()
        # wait for page loading
        WebDriverWait(
            self.driver,
            timeout=10
        ).until(EC.url_changes(start_url))
        # redirect to logout page: True or False?
        logout_url = self.home_url + "users/logout/"
        self.assertEqual(self.driver.current_url, logout_url)
