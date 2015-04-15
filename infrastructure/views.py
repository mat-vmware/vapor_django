from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from pyVim.connect import SmartConnect, Disconnect

def index(request):
    # return HttpResponse("Hi, guys. Please add a vCenter Server before doing anything.")
    template = loader.get_template('infrastructure/index.html')
    context = RequestContext(request, {
        'greeting': 'Hi, guys. Please add a vCenter Server before doing anything. BTW, I am from template.',
    })
    return HttpResponse(template.render(context))
