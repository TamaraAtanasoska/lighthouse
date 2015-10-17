from django.db import models

# Create your models here.


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
        ("AL", "All"),
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    ASPIRATION_CHOICES = (
        ("PM", "Product manager"),
        ("PR", "Programming"),
        ("DE", "Design"),
        ("AL", "All"),
    )
    aspiration = models.CharField(max_length=2, choices=ASPIRATION_CHOICES)
    GROUP_CHOICES = (
        ("ST", "Student"),
        ("UN", "Unemployed"),
        ("OT", "Other"),
        ("AL", "All"),
    )
    group = models.CharField(max_length=2, choices=GROUP_CHOICES)
    LEVEL_CHOICES = (
        ("BG", "Beginner"),
        ("IN", "Intermediate"),
        ("AD", "Advanced"),
        ("AL", "All"),
    )
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.name
