from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    subject_teaching = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(default=18, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
