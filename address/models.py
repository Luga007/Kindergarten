from django.db import models


class Address(models.Model):
    street_name = models.CharField(max_length=100)
    district_name = models.CharField(max_length=100, default='local')
    house_number = models.SmallIntegerField()

    def __str__(self):
        return self.street_name
