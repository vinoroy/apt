
from django.db import models

class Page(models.Model):


    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12,unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content',blank=True)

    def __str__(self):
        return self.title


class Sector(models.Model):
    sector = models.CharField(max_length=20)

    def __str__(self):
        return self.sector




class Property(models.Model):


    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, default='', null=True, blank=True)
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


class TypeService(models.Model):

    serviceName = models.CharField(max_length=20)
    type1 = models.CharField(max_length=40,default='',null=True,blank=True)
    type2 = models.CharField(max_length=40,default='',null=True,blank=True)
    type3 = models.CharField(max_length=40,default='',null=True,blank=True)
    type4 = models.CharField(max_length=40,default='',null=True,blank=True)


    def __str__(self):
        return self.serviceName



class Apartment(models.Model):


    sizeChoices = (
        ('1','3.5'),
        ('2','4.5'),
        ('3','5.5'),
    )


    statusChoices = (
        ('D', 'Disponible'),
        ('ND', 'Non disponible'),
    )

    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    aptNumber = models.CharField(max_length=4, default='', null=True, blank=True)

    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    sizes = models.CharField(max_length=3, choices=sizeChoices, default='1')
    #status = models.CharField(max_length=10,choices=statusChoices,default='D')

    serviceName = models.ForeignKey(TypeService, on_delete=models.SET_NULL, null=True)

    description = models.CharField(max_length=100,default='',null=True,blank=True)
    image1 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image2 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image3 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image4 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image5 = models.ImageField(upload_to='images/', default='',null=True,blank=True)
    image6 = models.ImageField(upload_to='images/', default='',null=True,blank=True)


    def __str__(self):
        return self.aptNumber
