from django.db import models
from django.urls import reverse


class User(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField()

    # def get_absolute_url(self):
    #     return reverse('get_user', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username

