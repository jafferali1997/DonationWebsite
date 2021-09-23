from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import  MinValueValidator
from django.contrib.auth.models import User

class Donation(models.Model):
    Name = models.CharField(max_length=200)
    Donating = models.CharField(max_length=200)
    Amount = models.IntegerField(default=1,validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.Name



class RequestForDonation(models.Model):
    Name = models.CharField(max_length=200)
    Purpose = models.TextField()
    CNIC = models.CharField(max_length=15)
    Address= models.CharField(max_length=500)
    Description = models.TextField()
    Contact_Number = models.CharField(max_length=16)
    Email = models.EmailField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_donation = models.BooleanField(default=False)

    def approve(self):
        self.approved_donation = True
        self.save()

    def get_absolute_url(self):
        return reverse("homepage")

    def __str__(self):
        return self.Purpose

class UserInfoModel(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
   

class AdminLoginModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    
    

