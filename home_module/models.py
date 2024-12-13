from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/uploads/slider_imgs/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
