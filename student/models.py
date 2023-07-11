from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50, default="Dennis")
    last_name = models.CharField(max_length=50, default="Akagha")
    address = models.CharField(max_length=256, default="No, 1 awoyemi street, ago palace way, okota")
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.first_name + " " + self.last_name
