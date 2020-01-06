#from django.urls import path

#from . import views


from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pages/pages/<str:name>', views.pages, name='pages'),
    path('pages/list/',views.list, name='list'),
    path('pages/detail/<int:id>',views.detail, name='detail'),
    path('pages/propos/',views.propos, name='propos'),
]