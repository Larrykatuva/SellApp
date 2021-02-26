from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.
class UserProfile(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    gender = models.CharField(max_length=50)
    birth_date = models.DateField(default=now)
    user_profile = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.owner
