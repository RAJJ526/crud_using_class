from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    student_id=models.IntegerField()
    total_marks=models.IntegerField()
    phone_no=models.IntegerField()