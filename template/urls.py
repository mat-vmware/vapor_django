from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<template_name>[0-9a-zA-Z_.-]+)/launch/$', views.launch, name='launch'),
    url(r'^vm/$', views.vm_list, name='vm_list'),
    url(r'^vm/new/$', views.vm_new, name='vm_new'),
]
