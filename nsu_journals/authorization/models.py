from django.db import models


class Student(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    is_super_user = models.BooleanField()

    def __str__(self):
        return self.email
