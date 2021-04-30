# from django.shortcuts import render, HttpResponse
from .models import User
from .forms import UserForm
# from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
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
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'user_update.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
