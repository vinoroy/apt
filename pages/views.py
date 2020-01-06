from django.shortcuts import render
from django.http import HttpResponse

from . models import Apartment, Property, Page

def index(request):
    #return HttpResponse("<h1>Bienvenue chez Logi 2001</h1>")

    aptList = Apartment.objects.all()
    propList = Property.objects.all()

    context = {'aptList': aptList, 'propList': propList}

    return render(request, "pages/index.html",context)



def pages(request,name):

    pagename = '/' + name
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        }

    return render(request, 'pages/pages.html', context)



def list(request):

    aptList = Apartment.objects.all()
    propList = Property.objects.all()

    context = {'aptList': aptList,'propList':propList}

    return render(request, 'pages/list.html',context)


def detail(request,id):

    #apt = Apartment.objects.get(id=id)

    apt = Apartment.objects.get(pk=id)

    context = {'apt': apt}

    return render(request, 'pages/detail.html', context)


def propos(request):

    return render(request, "pages/propos.html")

