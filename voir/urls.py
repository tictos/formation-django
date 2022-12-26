from django.urls import path
from voir.views import *


urlpatterns = [
    path('', home, name='accueil'),
    path('listing', listing, name='listing'),
    path('list', list, name= 'list')
]
