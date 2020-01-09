from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import json

def index(request):
    f = open('output.json')
    json_string = f.read()
    f.close()
    data = json.loads(json_string)
    #return HttpResponse("Ciao. Questa è la risposta.")
    return render(request, 'search/index.html', {'data': data})
