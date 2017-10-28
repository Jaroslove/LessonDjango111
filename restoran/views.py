from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Restorant


class RestoranListView(ListView):
    queryset = Restorant.objects.all()  # use object_list as list in templates
    template_name = 'restoran/home.html'


class SRestoranlist(ListView):
    queryset = Restorant.objects.filter(location__iexact='spb')  # use object_list as list in templates
    template_name = 'restoran/home.html'


class MRestoranlist(ListView):
    queryset = Restorant.objects.filter(location__iexact='moscow')  # use object_list as list in templates
    template_name = 'restoran/home.html'


def restorant_listview(request):
    template_name = 'restoran/home.html'
    queryset = Restorant.objects.filter(location__iexact='spb')
    context = {
        'list_restoran': queryset  # queryset.filter(location__iexact='spb')
    }
    return render(request, template_name, context)


def index(request):
    template = 'restoran/home.html'
    context = {
        'ee': [3, 24, 525, 35, 35]
    }
    return render(request, template, context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        template = 'restoran/home.html'
        context = {
            'ee': [3, 24, 525, 35, 35]
        }
        return render(request, template, context)


class ContactTemplateView(TemplateView):
    template_name = 'restoran/home.html'

    def get_context_data(self, *args, **kwargs):
        # context = super(ContactTemplateView, self).get_context_data(*args, **kwargs) show me the example of context
        context = {
            'ee': [3, 24, 525, 35, 35]
        }
        # print(context)
        return context
