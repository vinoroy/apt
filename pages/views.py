from django.shortcuts import render
from django.http import HttpResponse

from . models import Apartment, Property, Page,Size ,Sector



from django.core.mail import send_mail
from django.conf import settings


def index(request):

    submitted = ''

    # query the tabs of the application
    tabs = Page.objects.all()


    # get the query set of all the properties
    propList = Property.objects.all()

    # get the query set of all the appartment sizes and sectors to build the forms
    sizes = Size.objects.all()
    sectors = Sector.objects.all()


    # create an empty query
    aptFilter = []


    # if a post request was made
    if request.method == 'POST':


        # get the post request object
        p = request.POST

        # if the user requested a search
        if 'SEARCH' in p:

            # section to print post request results for degugging
            print(p)


            # get the search values for size and sector
            sizeList = p.getlist('sizeSel')
            sectorList = p.getlist('sectorSel')


            # execute the query based on the search values
            if not sizeList:

                aptFilter = Apartment.objects.filter(property__sector__sector__in=sectorList).filter(status__status='Disponible')

            elif not sectorList:

                aptFilter = Apartment.objects.filter(size__size__in=sizeList).filter(status__status='Disponible')

            else:

                aptFilter = Apartment.objects.filter(size__size__in=sizeList).filter(property__sector__sector__in=sectorList).filter(status__status='Disponible')

            # set the submitted value
            if not aptFilter:

                submitted = 'NoResult'

            else:

                submitted = 'Result'


        # if the user requested to send a message
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


    # if no post request, no special processing
    else:

        pass



    # prepare the context data for the reponse
    context = {'tabs': tabs, 'aptFilter': aptFilter, 'propList': propList, 'sizes': sizes, 'sectors': sectors, 'submitted': submitted}


    return render(request, "pages/index.html",context)




