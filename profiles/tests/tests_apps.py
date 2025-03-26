from django.test import TestCase
from django.apps import apps
from profiles.apps import ProfilesConfig


class ProfilesConfigTest(TestCase):
    """
    Test case for the ProfilesConfig class.

    This test case ensures that the ProfilesConfig class is correctly configured
    and that the application name is set properly.
    """

    def test_apps(self):
        """
        Test that the ProfilesConfig class is correctly configured.

        This test checks that the ProfilesConfig class is registered with the
        correct application name.
        """
        self.assertEqual(ProfilesConfig.name, "profiles")
        self.assertEqual(apps.get_app_config("profiles").name, "profiles")
