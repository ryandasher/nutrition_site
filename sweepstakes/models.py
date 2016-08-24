from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Drawing(models.Model):
    # A drawing can have many prizes.
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField("date created")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Prize(models.Model):
    # Many prizes belong to one drawing.
    value = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value)


@python_2_unicode_compatible
class Points(models.Model):
    # Point totals will need to belong to a user, but are also associated
    # with a drawing.
    value = models.IntegerField(default=0)
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value)


@python_2_unicode_compatible
class Winner(models.Model):
    # Record the winners, and make them independent of a drawing.
    winner = models.OneToOneField(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.winner)
