from django.db import models
from datetime import datetime


class News(models.Model):
    title = models.fields.CharField(max_length=1000, null=False, blank=False)
    story = models.fields.CharField(max_length=15000, null=False, blank=False)
    time = models.fields.TimeField(default=datetime.now())
