# -*- coding: utf-8 -*-
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search),

]