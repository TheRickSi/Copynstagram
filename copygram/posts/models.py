from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class Post(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=450)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    photo = models.ImageField(
        upload_to='posts/photo',
        blank=True,
        null=True
    )

    def __str__(self):
        user = User.objects.get(pk=self.profile.pk)
        return '{0} by @{1} '.format(self.title,user.username)
    