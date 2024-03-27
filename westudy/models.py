from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    rate = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return f'{self.name} by {self.teacher}'

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events/',default='')
    date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f'{self.name} at {self.date}'

class Feedback(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.TextField()

    def __str__(self):
        return f'Feedback by {self.username}'