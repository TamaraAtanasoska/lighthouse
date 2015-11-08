from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
 
class Aspiration(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    logo = models.ImageField(upload_to='profile_images', blank=True)
    link = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    category = models.ForeignKey(Category)
    aspiration = models.ManyToManyField(Aspiration)
    status = models.ManyToManyField(Status)
    level = models.ManyToManyField(Level)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

"""
class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='profile_images', blank=True)
    link = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    CATEGORY_CHOICES = (
        ("ME", "Meetup"),
        ("CO", "Conference"),
        ("UN", "Universities"),
        ("MS", "Mentorship"),
        ("JP", "Job portal"),
        ("LG", "Learners groups"),
        ("NT", "Networks"),
        ("HA", "Hackaton"),
        ("OT", "Other"),
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    ASPIRATION_CHOICES = (
        ("PM", "Product management"),
        ("PR", "Programming"),
        ("DE", "Product Design"),
        ("AL", "All"),
    )
    aspiration = models.CharField(max_length=2, choices=ASPIRATION_CHOICES)
    STATUS_CHOICES = (
        ("ST", "Student"),
        ("UN", "Unemployed"),
        ("OT", "Other"),
        ("AL", "All"),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    LEVEL_CHOICES = (
        ("BG", "Beginner"),
        ("IN", "Intermediate"),
        ("AD", "Advanced"),
        ("AL", "All"),
    )
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    GROUP_CHOICES = (
        ("FE", "Identified as female"),
        ("LG", "LGBTQI"),
        ("RA", "Race"),
    )
    group = models.CharField(max_length=2, choices=GROUP_CHOICES)

    def __str__(self):
        return self.name
"""
