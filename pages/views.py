from django.shortcuts import render
from django.http import HttpResponse

from . models import Apartment, Property, Page,Size ,Sector



from django.core.mail import send_mail
from django.conf import settings


def index(request):

    task = None
    submitted = ''

    tabs = Page.objects.all()


    aptList = Apartment.objects.all()
    propList = Property.objects.all()

    sizes = Size.objects.all()
    sectors = Sector.objects.all()


    aptFilter = []


    if request.method == 'POST':


        # get the post request object
        p = request.POST

        if 'SEARCH' in p:

            # section to print post request results for degugging
            print(p)
            #print(p.getlist('sizeSel'))
            #print(p.get('name'))


            # get the search values for size and sector
            sizeList = p.getlist('sizeSel')
            sectorList = p.getlist('sectorSel')


            # execute the query based on the search values
            if not sizeList:
                aptFilter = Apartment.objects.filter(property__sector__sector__in=sectorList)

            elif not sectorList:
                aptFilter = Apartment.objects.filter(size__size__in=sizeList)

            else:
                aptFilter = Apartment.objects.filter(size__size__in=sizeList).filter(property__sector__sector__in=sectorList)

            # set the submitted value
            submitted = 'Queries'


        elif 'MESSAGE' in p:

            # get the values for the contact form
            name = p.get('name')
            email = p.get('email')
            comments = p.get('comments')

            # send the email
            subject = 'Demande d`information de : ' + name + ' à : ' + email
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['logis2001info@gmail.com', ]
            send_mail(subject, comments, email_from, recipient_list)

            # set the submitted value to true
            submitted = 'Message'



    else:

        pass




    context = {'tabs': tabs, 'aptFilter': aptFilter, 'propList': propList, 'sizes': sizes, 'sectors': sectors, 'submitted': submitted}


    return render(request, "pages/index.html",context)




