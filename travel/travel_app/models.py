from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    dis=models.TextField()
    def __str__(self):
        return self.name
class profile(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    dis=models.TextField()
    def __str__(self):
        return self.name