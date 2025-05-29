from django.db import models
from group.models import Group
from django.core.exceptions import ValidationError


class Attendance(models.Model):
    date = models.DateField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='attendances')
    kids_arrived = models.IntegerField()

    def clean(self):
        total_arrived = sum(
            a.kids_arrived for a in self.group.attendances.exclude(id=self.id)
        )
        if total_arrived + self.kids_arrived > self.group.kids_quantity:
            raise ValidationError(
                f"The total number of children cannot exceed {self.group.kids_quantity}. "
                f"Already arrived: {total_arrived}, try add: {self.kids_arrived}."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'group: {self.group} arrived kids: {self.kids_arrived}'



