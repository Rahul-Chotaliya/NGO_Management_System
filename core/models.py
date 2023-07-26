from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

AbstractUser = User


# Create your models here.
class Donor(models.Model):
    name = models.TextField(max_length=20 )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.TextField(max_length=20 )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name


class Volunteer(models.Model):
    name = models.TextField(max_length=20 )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        ordering =['id']

class Otp(models.Model):
    otp = models.IntegerField(null=True)


class Project(models.Model):
    project_for = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField(default=datetime.now() )
    end_date = models.DateTimeField( )
    associated_volunteers = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    pic = models.FileField(null=True)
    # def __str__(self):
    #     return self.title

class Donation(models.Model):
    donation_for = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    upcoming_donation = models.CharField(max_length=500)
    name = models.TextField(max_length=200, null=True, default=None)
    about_donation = models.TextField(max_length=500, default=None, null=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donation_amount = models.IntegerField()
    pic = models.FileField(null=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    event_for = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    start_date = models.DateField(default=datetime.now())
    time = models.DateTimeField(default=datetime.now())
    location = models.CharField(max_length=500)
    associated_volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    pic = models.FileField(null=True)
    # def __str__(self):
    #     return self.title


