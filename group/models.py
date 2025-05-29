from django.db import models
from people.models import Caretaker



class Group(models.Model):
    group_name = models.CharField(max_length=50)
    caretakers = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    room = models.DecimalField(max_digits=5, decimal_places=2)
    total_quantity = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.group_name}"

    @property
    def kids_quantity(self):
        return self.total_quantity





