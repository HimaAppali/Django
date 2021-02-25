from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hima", views.hima, name='hima'),
    path("bindu", views.bindu, name='bindu'),
    #when ever a string with anyvalue is called then someone function will exicuted and it will pass name parameter from <str > to the someone method 
    path("<str:name>", views.somename, name='somename')
]