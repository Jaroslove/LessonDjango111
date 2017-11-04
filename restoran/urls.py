from django.conf.urls import url
from restoran import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.RestoranListView.as_view(), name='restoran'),
    url(r'^create/$', views.RestoranCreateView.as_view(), name='create_restoran'),
    # url(r'^restoran/create/$', views.restoran_createview),
    # url(r'^restoran/(?P<slug>\w+)$', views.SearchRestoranListView.as_view()),
    # url(r'^restoran/(?P<pk>\w+)$', views.DetailRestoranListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailRestoranListView.as_view(), name='details_restoran'),
    # use rest_id instead pk
    # url(r'^restoran/spb/$', views.SRestoranlist.as_view()),
    # url(r'^restoran/moscow/$', views.MRestoranlist.as_view()),
    # url(r'^home/', views.restorant_listview),
    # url(r'^home/(?P<id>\d+)', views.ContactTemplateView.as_view()),
    # url(r'^home/(?P<id>\d+)', views.ContactView.as_view()),
    # url(r'login/', LoginView.as_view(), name='login'),
]
