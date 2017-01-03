import requests
import json
import pocket

from .models import AccessToken

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render

def index(request):

    return_redirect_uri = 'http://127.0.0.1:8000/pocket_auth/process_pocket_redirect'

    request_token = pocket.Pocket.get_request_token(consumer_key=settings.POCKET_CONSUMER_KEY, redirect_uri=return_redirect_uri)
    request.session['POCKET_REQUEST_TOKEN'] = request_token

    pocket_auth_url = 'https://getpocket.com/auth/authorize?request_token=%s&redirect_uri=%s' % ( request_token, return_redirect_uri )

    return HttpResponseRedirect(pocket_auth_url)

def process_pocket_redirect(request):
    user_credentials = pocket.Pocket.get_credentials(consumer_key=settings.POCKET_CONSUMER_KEY, code=request.session.get('POCKET_REQUEST_TOKEN'))

    AccessToken.objects.all().delete()

    at = AccessToken()
    at.access_token = user_credentials['access_token']
    at.save()

    return HttpResponseRedirect('/')
