"""
Integration tests for the 'lettings' application views.
"""

from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting


class LettingViewsTest(TestCase):
    """
    Test case for the views in the 'lettings' application.
    """

    def setUp(self):
        """
        Set up test data for the views.
        """
        self.address = Address.objects.create(
            number=10,
            street="Main Street",
            city="Springfield",
            state="SP",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Cozy Apartment", address=self.address
        )

    def test_lettings_index_view(self):
        """
        Test the lettings index view.
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_letting_detail_view(self):
        """
        Test the letting detail view.
        """
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertContains(response, "Cozy Apartment")
