# """Contain the unit tests related to the models in app ``profiles``."""


# from django.test import TestCase

# from teamspirit.core.models import Address
# from teamspirit.profiles.models import Personal


# class PersonalModelTestsCase(TestCase):
#     """Test the model ``Personal``."""

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         address = Address(
#             label_first="1 rue de l'impasse",
#             label_second="",
#             postal_code=75000,
#             city="Paris",
#             country="France"
#         )
#         cls.personal_public = Personal(
#             first_name="Foo",
#             last_name="Dejoy",
#             phone_number="01 02 03 04 05",
#             address=address
#         )
#         cls.personal_public.save()
#         cls.personal_private = Personal(
#             first_name="Bar",
#             last_name="Tabba",
#             phone_number="05 04 03 02 01",
#             address=address
#         )
#         cls.personal_private.save()

#     def test_first_name(self):
#         """Unit test - app ``profiles`` - model ``Personal`` - #1.1

#         Test the first name.
#         """
#         pass
