from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Restorant
from .forms import RestoranCreateForm, RestoranCreateFromTwo
from django.http import HttpResponse, HttpResponseRedirect


@login_required()
def restoran_createview(request):
    form = RestoranCreateFromTwo(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/restoran/')
    if form.errors:
        print(form.errors)
    template_name = 'restoran/form.html'
    context = {'form': form}
    return render(request, template_name, context)


# def restoran_createview(request):
#     form = RestoranCreateForm(request.POST or None)
#     if form.is_valid():
#         obj = Restorant.objects.create(
#             name=form.cleaned_data.get('name'),
#             location=form.cleaned_data.get('location'),
#             category=form.cleaned_data.get('category')
#         )
#         return HttpResponseRedirect('/restoran/')
#     if form.errors:
#         print(form.errors)
#     template_name = 'restoran/form.html'
#     context = {'form': form}
#     return render(request, template_name, context)


class DetailRestoranListView(DetailView):
    queryset = Restorant.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(DetailRestoranListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(Restorant, id=rest_id)
    #     return obj


class SearchRestoranListView(ListView):
    template_name = 'restoran/home.html'

    def get_queryset(self):
        # print(self.kwargs)
        slug = self.kwargs.get('slug')
        print(slug)
        if slug:
            return Restorant.objects.filter(
                Q(location__iexact=slug) |
                Q(location__contains=slug)
            )
        else:
            return Restorant.objects.all()


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


class RestoranCreateView(LoginRequiredMixin, CreateView):
    form_class = RestoranCreateFromTwo
    login_url = '/login/'
    template_name = 'form.html'
    success_url = '/restoran/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save()
        return super(RestoranCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestoranCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add restoran'
        return context
