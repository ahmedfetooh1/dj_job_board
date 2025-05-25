from django.db import models

# Create your models here.
JOB_TYPE = (
    ('full time','full time'),
    ('part time','part time')
)
class JOb(models.Model):         #table
    #django model fields
        # - html widget
        # - validation
        # - db size 

    
    title = models.CharField(max_length=100)    #columns
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    #category
    experience = models.IntegerField(default=1)


    def ___str__(self):
        return self.title

