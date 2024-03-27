from django.db import models

# Create your models here.

class Datas(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=50, default="")
    phone_number = models.CharField(max_length=20, default="")  # Changed to CharField
    message = models.CharField(max_length=50, default="")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
    

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    services = models.CharField(max_length=100)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name    
