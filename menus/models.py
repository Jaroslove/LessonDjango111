from django.conf import settings
from django.db import models
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

    class Meta:
        ordering = ['-timestamp', '-update']

    def get_content(self):
        return self.contents.split(', ')

    def get_excludes(self):
        return self.excludes.split(', ')
