from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models


class Designation(models.Model):
    designation = models.CharField(max_length=36, blank=True, null=True, unique=True)
    designation_short = models.CharField(max_length=3, blank=True, null=True)
    grade = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.designation}'


genderChoice = [
    ('', '--Please Select--'),
    ('Male', 'Male'),
    ('Female', 'Female'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # bio = models.TextField(max_length=500, blank=True)
    father_name = models.CharField(max_length=128, null=True, blank=True)
    mother_name = models.CharField(max_length=128, null=True, blank=True)
    spouse_name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=genderChoice, null=True, blank=True)
    office_id = models.PositiveIntegerField(null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)
    birth_date = models.DateField(max_length=10, null=True, blank=True)
    joining_date = models.DateField(max_length=10, null=True, blank=True)
    office = models.CharField(max_length=128, null=True, blank=True)
    present_address = models.TextField(max_length=1000, null=True, blank=True)
    permanent_address = models.TextField(max_length=1000, null=True, blank=True)
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True)
    telephone = models.CharField(max_length=11, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=128, blank=True, null=True, unique=True)
    photo = models.ImageField(upload_to='user/profile/', null=True, blank=True)
    signature = models.ImageField(upload_to='user/sign/', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
