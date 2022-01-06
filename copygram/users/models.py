from django.db import models
from django.contrib.auth.models import User

#Models.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(max_length=100)
    email = models.EmailField()
    biography= models.TextField(blank=True)
    phone = models.CharField(max_length=20,blank=True)
    picture = models.ImageField(
        'users/pictures',
        blank=True,
        null=True
    )
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username