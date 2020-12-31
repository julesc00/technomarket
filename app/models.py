from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def clean(self):
        """Return name capitalize formatted."""
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    new = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    made_date = models.DateField()

    def clean(self):
        """Return name capitalize formatted."""
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name
