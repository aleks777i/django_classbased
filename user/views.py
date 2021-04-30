from .models import User
from .forms import UserForm
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, CreateView, FormView, DetailView


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class UserAddView(CreateView):
    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '/'


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_update.html'
    success_url = '/'


class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

