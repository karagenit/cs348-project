from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Fraternity(models.Model):
    # automatically generates an ID#
    name = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)

class Student(models.Model):
    puid = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length = 200)
    email = models.EmailField(blank = True)
    phone = PhoneNumberField(blank = True)
    major = models.CharField(max_length = 200, blank = True)
    gpa   = models.DecimalField(max_digits = 3, decimal_places = 2, null = True)
    hometown = models.CharField(max_length = 200, blank = True)
    
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADE_CHOICES = [(FRESHMAN, 'Freshman'),(SOPHOMORE, 'Sophomore'),(JUNIOR, 'Junior'),(SENIOR, 'Senior & Above'),]
    grade = models.CharField(max_length = 2, choices = GRADE_CHOICES, blank = True)

class Event(models.Model):
    name = models.CharField(max_length = 200)
    date = models.DateField(db_index = True)
    host = models.ForeignKey(Fraternity, on_delete = models.CASCADE)
    attendees = models.ManyToManyField(Student)
