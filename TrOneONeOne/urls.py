from django.conf.urls import url
from django.contrib import admin
from restoran import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restoran/$', views.RestoranListView.as_view()),
    url(r'^restoran/(?P<slug>\w+)$', views.SearchRestoranListView.as_view()),
    # url(r'^restoran/spb/$', views.SRestoranlist.as_view()),
    # url(r'^restoran/moscow/$', views.MRestoranlist.as_view()),
    # url(r'^home/', views.restorant_listview),
    # url(r'^home/(?P<id>\d+)', views.ContactTemplateView.as_view()),
    # url(r'^home/(?P<id>\d+)', views.ContactView.as_view()),
]