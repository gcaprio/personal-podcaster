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


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


class Command(BaseCommand):
        help = 'Imports All Assessments'

        def handle(self, *args, **options):

            undownloaded_pocket_items = PocketItem.objects.filter(
                downloaded_file=''
            )[:1]

            ydl_opts = {
                'format': 'bestaudio/best',
                'extractaudio': True,
                'print_debug_header': settings.DEBUG,
                'verbose': settings.DEBUG,
                #'logger': Logger(),
                #'progress_hooks': [my_hook],
            }

            for pocket_item in undownloaded_pocket_items:
                resolved_title_hash = hashlib.md5(pocket_item.resolved_title.encode())

                ydl_opts['outtmpl'] = '%s/%s.mp3' % ( settings.MEDIA_ROOT, unicode(resolved_title_hash.hexdigest()))

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([pocket_item.resolved_url])

                    pocket_item.downloaded_file = resolved_title_hash.hexdigest()

                    pocket_item.save()
