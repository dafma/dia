from django.conf.urls import url
from django.contrib import admin

from .views import (
    cabecera,
detallecabecera)

urlpatterns = [
    url(r'^$',cabecera, name='solopanel1'),
    url(r'^referencia/(?P<ID>\d+)/$',detallecabecera,name='detallecabecera'),
    ]
