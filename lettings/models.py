"""
Module containing the models for the 'lettings' application.

This module defines the core models for storing address and rental information.
"""

from django.db import models
import sentry_sdk


class Address(models.Model):
    """
    Model representing a postal address.

    Attributes:
        number (int): Street number.
        street (str): Street name.
        city (str): City name.
        state (str): State code (2 letters).
        zip_code (int): Zip code.
        country_iso_code (str): Country ISO code (3 letters).
    """

    number = models.PositiveIntegerField()
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
    country_iso_code = models.CharField(max_length=3)

    def __str__(self):
        """
        Returns a readable representation of the address.

        Returns:
            str: Formatted address string.
        """
        try:
            return (
                f"{self.number} {self.street}, {self.city} "
                f"{self.state} {self.zip_code}, {self.country_iso_code}"
            )
        except Exception as e:
            sentry_sdk.capture_exception(e)
            return "Invalid Address"

    class Meta:
        """
        Metadata for the Address model.

        Attributes:
            verbose_name_plural (str): Defines the plural name displayed in the Django admin.
        """

        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Model representing a rental property associated with an address.

    Attributes:
        title (str): Rental property title.
        address (Address): Associated address (OneToOne relation).
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a readable representation of the rental property.

        Returns:
            str: The title of the rental property.
        """
        try:
            return self.title
        except Exception as e:
            sentry_sdk.capture_exception(e)
            return "Unknown Letting"
