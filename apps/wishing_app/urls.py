from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^jobs/new$', views.new_job),
    url(r'^add_job$', views.add_job), #processing route
    url(r'^jobs/(?P<id>\d+)$', views.display_job),
    url(r'^jobs/edit/(?P<id>\d+)$', views.edit_job),
    url(r'^delete_job/(?P<id>\d+)$', views.delete_job), #processing route
    url(r'^edit_job/(?P<id>\d+)$', views.edits), #processing route
    url(r'^logout$', views.logout) #processing route
]