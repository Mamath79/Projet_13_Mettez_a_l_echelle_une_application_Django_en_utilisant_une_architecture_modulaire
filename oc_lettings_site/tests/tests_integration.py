from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Address, Letting
from profiles.models import Profile
from django.contrib.auth.models import User
import sentry_sdk


class IntegrationTest(TestCase):
    """
    Test case for integration testing of the 'oc_lettings_site' application.
    """

    def setUp(self):
        """
        Configure the test database with example data.
        """
        self.client = Client()

        # Création d'un utilisateur
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Création d'une adresse et d'un letting
        self.address = Address.objects.create(
            number=123, street="Rue Test", city="Paris",
            state="FR", zip_code=75001, country_iso_code="FR"
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

        # Création d'un profil utilisateur
        self.profile = Profile.objects.create(user=self.user, favorite_city="Lyon")

    def test_index_page(self):
        """
        Vérifie que la page d'accueil est accessible et contient les bons éléments.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test changement")

    def test_letting_detail_page(self):
        """
        Vérifie l'accès à une annonce et l'affichage des détails.
        """
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")

    def test_profile_page(self):
        """
        Vérifie que la page de profil affiche bien les informations.
        """
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lyon")

    def test_404_error_handling(self):
        """
        Vérifie que la gestion des erreurs 404 fonctionne correctement.
        """
        response = self.client.get("/page-inexistante/")
        self.assertEqual(response.status_code, 404)

    def test_sentry_error_logging(self):
        """
        Simule une erreur pour vérifier que Sentry capture bien l'exception.
        """
        try:
            1 / 0  # Provoquer une division par zéro
        except Exception as e:
            sentry_sdk.capture_exception(e)

        # Normalement, l'erreur doit apparaître dans Sentry
