from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.png', upload_to='profile_photos')
  bio = models.TextField(blank=True, null=True, max_length=200)

  def __str__(self):
    return f'User {self.user.username}\'s profile'
  
  # # resizing big image
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    img=Image.open(self.image.path)

    if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
