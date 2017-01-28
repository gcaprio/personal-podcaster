from __future__ import unicode_literals

from django.db import models


class AccessToken(models.Model):
    access_token = models.TextField()


class PocketItem(models.Model):
    pocket_id = models.IntegerField()
    given_title = models.TextField()
    given_url = models.URLField()
    resolved_id = models.IntegerField()
    resolved_title = models.TextField()
    resolved_url = models.URLField()
    downloaded_file = models.FileField(upload_to='pocket_items', blank=None, null=True)
