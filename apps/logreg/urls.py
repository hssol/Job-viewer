from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.logreg),
    url(r'^register_account$', views.register),
    url(r'^login_account$', views.login)
]