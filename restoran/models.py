from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slag_generator


class Restorant(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name  # obj.title


def r_pre_save_receiver(sender, instance, *args, **kwargs):
    # print('saving...')
    # print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slag_generator(instance)


# def r_post_save_receiver(sender, created, instance, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)


pre_save.connect(r_pre_save_receiver, sender=Restorant)
# post_save.connect(r_post_save_receiver, sender=Restorant)
