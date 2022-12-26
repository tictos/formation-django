
from django.urls import path
from utilisat.views import *

urlpatterns = [
    path('', listdiffuse, name="diffusion"),
    path('<int:pk>', email_detail, name='detail')
]
