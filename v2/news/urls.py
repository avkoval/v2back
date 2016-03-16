from django.conf.urls import patterns, url
from django.contrib import admin
from .views import HomeView

admin.autodiscover()

urlpatterns = patterns(
    'home.views',
    url('', HomeView, name='home'),
)
