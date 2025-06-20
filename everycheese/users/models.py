from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.db import models
# Create your models here.

class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )
    bio=models.TextField("bio",blank=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )
