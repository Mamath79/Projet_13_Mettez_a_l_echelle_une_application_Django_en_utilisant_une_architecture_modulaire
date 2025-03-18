from django.db import models


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
    country_iso_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.number} {self.street}, {self.city}, {self.state} {self.zip_code}, {self.country_iso_code}"


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
