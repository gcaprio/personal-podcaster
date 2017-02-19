# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel


class AccessToken(TimeStampedModel):
    access_token = models.TextField()


class PocketItem(TimeStampedModel):
    pocket_id = models.IntegerField()
    given_title = models.TextField()
    given_url = models.URLField(max_length=4096)
    resolved_id = models.IntegerField()
    resolved_title = models.TextField()
    resolved_url = models.URLField(max_length=4096)
    downloaded_file = models.FileField(upload_to='pocket_items', blank=None, null=True, default='')

    def __unicode__(self):
        return self.resolved_title
