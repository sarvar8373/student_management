from django.db import models

class student(models.Model):
  student_number = models.PositiveIntegerField()
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=100)
  fiel_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()

  def __str__(self):
    return f'student:  {self.firstname} {self.lastname}'