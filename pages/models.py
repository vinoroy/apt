
from django.db import models

class Page(models.Model):


    menuTitle = models.CharField(max_length=20,default='', null=True, blank=True)
    title = models.CharField(max_length=60)
    bodytext = models.TextField('Page Content',blank=True)
    bodytext2 = models.TextField('Page Content', blank=True)
    image = models.ImageField(upload_to='images/', default='')
    update_date = models.DateTimeField('Last Updated')


    # REMOVE
    permalink = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.title


class Sector(models.Model):
    sector = models.CharField(max_length=20)

    def __str__(self):
        return self.sector




class Property(models.Model):


    name = models.CharField(max_length=30)
    description = models.TextField('Page Content',default='', null=True, blank=True)
    numberApts = models.CharField(max_length=100, default='', null=True, blank=True)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal = models.CharField(max_length=30)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/',default='')


    def __str__(self):
        return self.name



class Size(models.Model):

    size = models.CharField(max_length=4)

    def __str__(self):
        return self.size


class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class Services(models.Model):

    services = models.CharField(max_length=200)

    def __str__(self):
        return self.services



class Apartment(models.Model):


    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    aptNumber = models.CharField(max_length=4, default='', null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    services = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=100,default='',null=True,blank=True)

    image1 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image1Text = models.CharField(max_length=50, default='', null=True, blank=True)

    image2 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image2Text = models.CharField(max_length=50, default='', null=True, blank=True)

    image3 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image3Text = models.CharField(max_length=50, default='', null=True, blank=True)

    image4 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image4Text = models.CharField(max_length=50, default='', null=True, blank=True)

    image5 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image5Text = models.CharField(max_length=50, default='', null=True, blank=True)

    image6 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image6Text = models.CharField(max_length=50, default='', null=True, blank=True)


    def __str__(self):
        return self.aptNumber
