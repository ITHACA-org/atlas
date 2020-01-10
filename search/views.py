from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import json
import requests

def index(request):
    response = requests.get('https://catalogue.onda-dias.eu/dias-catalogue/Products?$search="name:*"&$top=3')
    data = response.json()
    return render(request, 'search/index.html', {'data': data})
