from tkinter import image_names
from django.db import models

# Create your models here.
    #django model fields
        # - html widget
        # - validation
        # - db size 
class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


JOB_TYPE = (
    ('full time','full time'),
    ('part time','part time')
)
def image_upload(instance,filename):
    imagenamme , extension = filename.split(".")
    return 'jobs/%s.%s' %(instance.id,extension)


class JOB(models.Model):         #table


    
    title = models.CharField(max_length=100)    #columns
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload)



    def ___str__(self):
        return self.title

