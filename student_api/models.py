from django.db import models

# Create your models here.
class Students(models.Model):

    GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("U", "Undisclosed"),
    ]

    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    percentage = models.FloatField()

    institute = models.ForeignKey("Institute", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



class Institute(models.Model):

    INSTITUTE_TYPE_CHOICES = [
    ("C", "College"),
    ("H", "High School"),
    ]

    name = models.CharField(max_length=100)
    institute_type = models.CharField(max_length=1, choices=INSTITUTE_TYPE_CHOICES)

    def __str__(self):
        return self.name