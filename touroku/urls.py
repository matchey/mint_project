from django.conf.urls import url
from . import views

app_name = 'touroku'
urlpatterns = [
    url(r'^$', views.TourokuView.touroku, name='touroku'),
    url(r'1/$', views.ListView.lists, name='lists'),
    # url(r'^(?P<pk>[0-9]+)/$', views.ListView.lists, name='lists'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<kansuu_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
