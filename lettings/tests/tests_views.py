from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Address, Letting

class LettingsViewTest(TestCase):
    """
    Test the Lettings views.
    """
    def setUp(self):
        """
        Set up the test environment for LettingsViewTest.
        Create an instance of Address with test values.
        """
        self.client = Client()
        self.address = Address.objects.create(
            number=1, street="Main Street", city="Paris",
            state="FR", zip_code=75001, country_iso_code="FR"
        )
        self.letting = Letting.objects.create(title="Nice House", address=self.address)

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
        self.assertContains(response, "Nice House")
