# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       # Detail Slider View
                       url(r'^(?P<img_id>\d+)$', views.image_slider, name="image_slider"),
                       )
