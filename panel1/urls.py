from django.conf.urls import url
from django.contrib import admin

from .views import (
    panel1
    )

urlpatterns = [
    url(r'^$', panel1, name='solopanel1'),


    ]
