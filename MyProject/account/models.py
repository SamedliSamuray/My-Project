from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfilPicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True,default='profil_picture/unnamed.jpg',upload_to='profil_picture')
    phone = models.CharField(blank=True,default='',max_length=20)
    user_address = models.CharField(blank=True,default='',max_length=20)
    def __str__(self) :
        return self.user.username
