from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)
    def __str__(self):
        return self.real_name

class Activity_periods(models.Model):
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end_time')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_periods')



