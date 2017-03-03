# coding=utf-8
from __future__ import unicode_literals

import hashlib
import youtube_dl

from pocket_auth.models import PocketItem

from django.core.management import BaseCommand
from django.conf import settings


class Logger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

# TODO: Skip over playlists for now
class Command(BaseCommand):

        def handle(self, *args, **options):

            ydl_opts = {
                'format': 'bestaudio',
                'extractaudio': True,
                'print_debug_header': settings.DEBUG,
                'verbose': settings.DEBUG,
                #'logger': Logger(),
            }

            #pocket_items_to_be_downloaded = PocketItem.objects.filter(
            #    downloaded_file=''
            #)[:1]

            pocket_items_to_be_downloaded = PocketItem.objects.filter(
                id=3
            )[:1]

            for pocket_item in pocket_items_to_be_downloaded:
                print pocket_item
                try:
                    resolved_title_hash = hashlib.md5(pocket_item.resolved_title.encode())

                    ydl_opts['outtmpl'] = '%s/%s' % (settings.MEDIA_ROOT, unicode(resolved_title_hash.hexdigest())) + '.%(ext)s'
                    #ydl_opts['outtmpl'] = '%s/%(title)s.f%(format_id)s.%(ext)s' % (settings.MEDIA_ROOT)
                    #ydl_opts['outtmpl'] = settings.MEDIA_ROOT + '/%(title)s.f%(format_id)s.%(ext)s'

                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([pocket_item.resolved_url])

                        pocket_item.downloaded_file = resolved_title_hash.hexdigest()

                        pocket_item.save()
                except:
                    pass
