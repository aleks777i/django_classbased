# from django.shortcuts import render, HttpResponse
from user.models import User
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, View, FormView, DetailView


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
