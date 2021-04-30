"""patstavigais_darbs_11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import UserListView, UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserListView.as_view()),
    path('get_user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # path('add_user', UserCreateView.as_view(), name='add_user'),
    # path('user/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    # path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
