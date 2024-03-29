from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to= 'basic_app/profile_pics',blank=True)

    def __self__(self):
        return self.user.username
