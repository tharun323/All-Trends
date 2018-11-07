from django.conf.urls import url
from views import *

urlpatterns = [

    url(r'headlines/',headlines),
    url(r'newssources/',newssources)
]