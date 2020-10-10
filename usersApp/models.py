from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(blank=False, max_length=100)
    photo = models.ImageField(upload_to='photos')


    def __str__(self):
        return self.email
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwrgs):
    if created:
        Token.objects.create(user=instance)