from __future__ import unicode_literals
import youtube_dl

from django.core.management import BaseCommand

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

class Command(BaseCommand):
        help = 'Imports All Assessments'

        def handle(self, *args, **options):
            video_url = 'https://www.youtube.com/watch?v=wewAC5X_CZ8&feature=youtu.be'

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'logger': MyLogger(),
                'progress_hooks': [my_hook],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
