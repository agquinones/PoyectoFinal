from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from .forms import PageForm

#Create your views here.
class PageListView(ListView):
    model=Page

class PageDetailView(DetailView):
    model=Page

class PageCreate(LoginRequiredMixin,CreateView):
    model = Page
    form_class = PageForm
    success_url=reverse_lazy('pages:pages')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdate(LoginRequiredMixin,UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages:pages')

class PageDelete(LoginRequiredMixin,DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')