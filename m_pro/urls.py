from django.urls import path
from .import views

urlpatterns = [
    #path('',views.index,name='home'),
     path('',views.index, name='home'),
     path('contact/',views.contact, name='contact'),
     path('about/',views.Myself, name='about'),
     path('showdata/',views.showdata, name='showdata')

]
