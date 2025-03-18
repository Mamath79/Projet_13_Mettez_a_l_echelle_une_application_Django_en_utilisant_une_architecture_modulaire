"""
Unit tests for the 'lettings' application models.
"""

from django.test import TestCase
from lettings.models import Address, Letting


class AddressModelTest(TestCase):
    """
    Test case for the Address model.
    """

    def setUp(self):
        """
        Set up a test Address instance.
        """
        self.address = Address.objects.create(
            number=42,
            street="Baker Street",
            city="London",
            state="LD",
            zip_code=12345,
            country_iso_code="GBR"
        )

    def test_address_str(self):
        """
        Test the __str__ method of Address.
        """
        expected_str = "42 Baker Street, London LD 12345, GBR"
        self.assertEqual(str(self.address), expected_str)


class LettingModelTest(TestCase):
    """
    Test case for the Letting model.
    """

    def setUp(self):
        """
        Set up a test Letting instance.
        """
        self.address = Address.objects.create(
            number=99,
            street="Sunset Boulevard",
            city="Los Angeles",
            state="CA",
            zip_code=90028,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(
            title="Luxury Villa",
            address=self.address
        )

    def test_letting_str(self):
        """
        Test the __str__ method of Letting.
        """
        self.assertEqual(str(self.letting), "Luxury Villa")
