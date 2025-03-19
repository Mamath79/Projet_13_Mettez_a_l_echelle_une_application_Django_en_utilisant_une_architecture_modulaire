from django.test import TestCase
from lettings.models import Address, Letting

class AddressModelTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for AddressModelTest.
        Create an instance of Address with test values.
        """
        self.address = Address.objects.create(
            number=123, street="Rue Test", city="Paris",
            state="FR", zip_code=75001, country_iso_code="FR"
        )

    def test_address_str(self):
        """
        Test the __str__ method of Address.
        Verify that the string representation of the address is correct.
        """
        expected_str = "123 Rue Test, Paris FR 75001, FR"
        self.assertEqual(str(self.address), expected_str)

    def test_address_str_error(self):
        """
        Test the exception handling in __str__ of Address.
        Ensures that if an error occurs, the return value is 'Invalid Address'.
        """
        # On simule une erreur en mettant une valeur None dans un champ nécessaire
        self.address.street = None
        self.assertEqual(str(self.address), "Invalid Address")


class LettingModelTest(TestCase):
    """
    Test the Letting model.
    """
    def setUp(self):
        """
        Set up the test environment for LettingModelTest.
        Create an instance of Address with test values.
        """
        self.address = Address.objects.create(
            number=456, street="Avenue Test", city="Lyon",
            state="FR", zip_code=69001, country_iso_code="FR"
        )
        self.letting = Letting.objects.create(title="Super Letting", address=self.address)

    def test_letting_str(self):
        """
        Test the __str__ method of Letting.
        Verify that the string representation of the letting is correct.
        """
        self.assertEqual(str(self.letting), "Super Letting")

    def test_letting_str_error(self):
        """
        Test the exception handling in __str__ of Letting.
        Ensures that if an error occurs, the return value is 'Unknown Letting'.
        """
        # On simule une erreur en mettant une valeur None dans un champ nécessaire
        self.letting.title = None
        self.assertEqual(str(self.letting), "Unknown Letting")
