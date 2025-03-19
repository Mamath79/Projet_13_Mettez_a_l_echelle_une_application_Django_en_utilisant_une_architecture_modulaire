from django.test import TestCase
from django.apps import apps
from lettings.apps import LettingsConfig


class LettingsConfigTest(TestCase):
    """
    Test case for the LettingsConfig class.

    This test case ensures that the LettingsConfig class is correctly configured
    and that the application name is set properly.
    """

    def test_apps(self):
        """
        Test that the LettingsConfig class is correctly configured.

        This test checks that the LettingsConfig class is registered with the
        correct application name.
        """
        self.assertEqual(LettingsConfig.name, "lettings")
        self.assertEqual(apps.get_app_config("lettings").name, "lettings")
