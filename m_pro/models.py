from django.db import models

# Create your models here.

# class add_account(models.Model):
#     id_no = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20)
#     fathers_name = models.CharField(max_length=20)
#     address = models.CharField(max_length=20)

# class dep_amount(models.Model):
#     id_no = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20)
#     amount = models.CharField(max_length=20)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    

    def __str__(self):
        return self.name