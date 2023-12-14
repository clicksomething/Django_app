from django.db import models
gender_choices = [
    ("F", "Female"),
    ("M", "Male")
]
class person(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length= 100)
    middle_name = models.CharField(max_length=100)
    gender=models.CharField(max_length=20,choices=gender_choices)


