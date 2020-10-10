from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(blank=False, max_length=100)
    photo = models.ImageField(upload_to='photos')
    


    def __str__(self):
        return self.email
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

