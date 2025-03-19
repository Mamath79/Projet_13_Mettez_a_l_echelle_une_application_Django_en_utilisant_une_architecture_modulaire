import sentry_sdk
from django.db import models


class Address(models.Model):
    """
    Model representing a postal address.
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
        """
        try:
            if not all([self.number, self.street, self.city, self.state, self.zip_code, self.country_iso_code]):
                raise ValueError("Missing required fields")
            return f"{self.number} {self.street}, {self.city} {self.state} {self.zip_code}, {self.country_iso_code}"
        except Exception as e:
            sentry_sdk.capture_exception(e)
            return "Invalid Address"


class Letting(models.Model):
    """
    Model representing a rental property associated with an address.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a readable representation of the rental property.
        """
        try:
            if not self.title:
                raise ValueError("Title is missing")
            return self.title
        except Exception as e:
            sentry_sdk.capture_exception(e)
            return "Unknown Letting"
