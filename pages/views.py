from django.shortcuts import render
from django.http import HttpResponse

from . models import Apartment, Property, Page,Size ,Sector

from .forms import SizeForm, SectorForm

def index(request):
    #return HttpResponse("<h1>Bienvenue chez Logi 2001</h1>")

    task = None
    submitted = False

    tabs = Page.objects.all()


    aptList = Apartment.objects.all()
    propList = Property.objects.all()

    sizes = Size.objects.all()
    sectors = Sector.objects.all()


    aptFilter = []


    if request.method == 'POST':

        print('post received')

        p = request.POST

        print(p)

        print(p.getlist('sizeSel'))

        sizeList = p.getlist('sizeSel')

        sectorList = p.getlist('sectorSel')


        if not sizeList:
            aptFilter = Apartment.objects.filter(property__sector__sector__in=sectorList)

        elif not sectorList:
            aptFilter = Apartment.objects.filter(size__size__in=sizeList)

        else:
            aptFilter = Apartment.objects.filter(size__size__in=sizeList).filter(property__sector__sector__in=sectorList)


        submitted = True



    else:

        pass


    context = {'tabs': tabs, 'aptFilter': aptFilter, 'propList': propList, 'sizes': sizes, 'sectors': sectors, 'submitted': submitted}


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

