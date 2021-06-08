from django.db import models


class Project_class(models.Model):
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date=models.DateField(auto_now=False)

    def __str__(self):
        return self.title