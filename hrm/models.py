from django.db import models

# Create your models here.
class Users(models.Model):
    #employee_id = models.CharField(max_length=10, null=True, blank=True) if we want field to be optional
    employee_id = models.CharField(max_length=10, unique =True)
    name= models.CharField(max_length=100)#Rajiv sharma
    age = models.IntegerField()#32
    ranking = models.FloatField()#2.5

    def upload_photo(self,filename):
        path='hrm/photo/{}'.format(filename)
        return path

    photo = models.ImageField(upload_to=upload_photo, null= True, blank =True) #optional field

    def upload_file(self,filename):
        path='hrm/file/{}'.format(filename)
        return path

    resume = models.ImageField(upload_to=upload_file, null = True, blank = True) #this is optional

    def __str__(self): #this help to visualize the database.
        return f"{self.employee_id} - {self.name}" # used to show username insted of Users Object(1) in administration.