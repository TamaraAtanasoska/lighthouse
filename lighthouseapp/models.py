from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='profile_images', blank=True)
    link = models.CharField(max_length=150)
    city = models.CharField(max_length=150, null=True)
    country = CountryField(blank_label='(Select Country)')
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
        ("AL", "All"),
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    ASPIRATION_CHOICES = (
        ("PM", "Product manager"),
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
        ("AL", "All"),
    )
    group = models.CharField(max_length=2, choices=GROUP_CHOICES)

    def __str__(self):
        return self.name
