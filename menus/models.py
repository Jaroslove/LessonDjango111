from django.conf import settings
from django.db import models
from django.urls import reverse

from restoran.models import Restorant


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restoran = models.ForeignKey(Restorant)
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='this is help')
    excludes = models.TextField(blank=True, null=True, help_text='another')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details_menus', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-timestamp', '-update']

    def get_content(self):
        return self.contents.split(', ')

    def get_excludes(self):
        return self.excludes.split(', ')
