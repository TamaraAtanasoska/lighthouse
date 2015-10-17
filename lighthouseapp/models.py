from django.db import models

# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='profile_images', blank=True)
    # link =
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
        ("PM", "Product manager"),
        ("PR", "Programming"),
        ("DE", "Design"),
    )
    aspiration = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    GROUP_CHOICES = (
        ("ST", "Student"),
        ("UN", "Unemployed"),
        ("OT", "Other"),
    )
    group = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    LEVEL_CHOICES = (
        ("BG", "Beginner"),
        ("IN", "Intermediate"),
        ("AD", "Advanced"),
    )
    level = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
