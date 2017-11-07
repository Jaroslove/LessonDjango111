from django.conf.urls import url
from .views import ItemListView, ItemCreateView, ItemDetailView, ItemUpdateView

urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='menus'),
    url(r'^create/$', ItemCreateView.as_view(), name='create_menus'),
    url(r'^(?P<pk>[\w-]+)/$', ItemDetailView.as_view(), name='details_menus'),
]
