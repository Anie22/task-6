from tokenize import Name
from django.db import models


# Create your models here.

class XYZ_Hotel(models.Model):
  Occupant_Name = models.CharField(max_length=90)
  Occupant_Email = models.EmailField(max_length=254)
  Occupant_Occupation = models.CharField(max_length=90)
  Room_number = models.IntegerField()
  Amount_paid = models.CharField(max_length=70)
  Number_of_night = models.IntegerField()
  Start_date = models.DateField()
  End_date = models.DateField()
  
  def __str__(self):
        return self.Occupant_Name
 
      

      

