"""
Module containing the models for the 'profiles' application.

This module defines the models for managing user profiles and their preferences.
"""

from django.db import models
from django.contrib.auth.models import User
import sentry_sdk


class Profile(models.Model):
    """
    Model representing a user profile with additional information.

    This model extends the Django User model with additional fields specific
    to the application's needs.

    Attributes:
        user (User): One-to-one relationship with Django's User model.
        favorite_city (str): User's favorite city (optional).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a readable representation of the profile.

        Returns:
            str: The username of the associated user.
        """
        try:
            return self.user.username
        except Exception as e:
            sentry_sdk.capture_exception(e)
            return "Unknown User"

    class Meta:
        """
        Metadata for the Profile model.

        Attributes:
            verbose_name_plural (str): Defines the plural name displayed in the Django admin.
        """

        verbose_name_plural = "Profiles"
