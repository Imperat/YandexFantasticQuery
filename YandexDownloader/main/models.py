from django.db import models
from django.utils import timezone


class YandexEntity(models.Model):
    page_number = models.IntegerField()
    url = models.URLField(null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        return super(YandexEntity, self).save(*args, **kwargs)
