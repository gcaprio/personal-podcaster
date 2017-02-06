# coding=utf-8
from __future__ import unicode_literals

import pocket

from pocket_auth.models import AccessToken, PocketItem

from django.core.management import BaseCommand
from django.conf import settings

# TODO: Update get to include since parameter.
class Command(BaseCommand):
        help = 'Downloads Latest Items from Pocket'

        def handle(self, *args, **options):
            at = AccessToken.objects.all()[0]

            pocket_instance = pocket.Pocket(settings.POCKET_CONSUMER_KEY, at.access_token)

            response, headers = pocket_instance.get(contentType='video', wait=False)

            items_list = response['list']

            for id in items_list:
                item = items_list[id]
                if PocketItem.objects.filter(pocket_id=id).exists():
                    pocket_item = PocketItem.objects.get(pocket_id=id)
                else:
                    pocket_item = PocketItem()
                if item['has_video'] != '2':
                    continue
                pocket_item.given_title = item['given_title']
                pocket_item.given_url = item['given_url']
                pocket_item.resolved_id = item['resolved_id']
                pocket_item.resolved_title = item['resolved_title']
                pocket_item.resolved_url = item['resolved_url']
                pocket_item.pocket_id = item['item_id']
                pocket_item.save()
