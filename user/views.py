# from django.shortcuts import render, HttpResponse
from .models import User
from .forms import UserForm
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, View, FormView, DetailView


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class UserAddView(FormView):
    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form)
        return response