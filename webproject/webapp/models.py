from django.db import models

# Create your models here.
class places(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
    discr=models.TextField()
    def __str__(self):
        return self.name
class team(models.Model):
    name=models.CharField(max_length=200)
    disc=models.TextField()
    img=models.ImageField(upload_to='teamimage')
    def __str__(self):
        return self.name
