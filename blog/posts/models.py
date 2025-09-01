from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Form(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField()
     phone_number = models.IntegerField()
     about = models.TextField()