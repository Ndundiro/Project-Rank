from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    sitename = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url= models.CharField(max_length=50)
    screenshot = models.ImageField(upload_to = 'screenshots', default = 'default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted = models.DateTimeField(auto_now_add=True)
    design = models.IntegerField(blank=True,default=7.0)
    usability = models.IntegerField(blank=True,default=7.0)
    overall = models.IntegerField(blank=True,default=7.0)

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
    
    def __str__(self):
        return self.sitename
