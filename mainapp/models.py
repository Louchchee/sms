from django.db import models
from django.contrib.auth.models import AbstractUser

#Overriding Default USER
class CustomUser(AbstractUser):
    data = (
        (1,"Manager"), 
        (2, "Teachers"), 
        (3, "Students")
    )
    user_type = models.CharField(default=1, choices=data, max_length=10)



class Manager(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    objects = models.Manager()
 

class Teachers(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Teachers"


    def __str__(self):
        return self.admin.username

        


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    customuser = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    # middleName = models.CharField(max_length=40, null=True, blank=True)
    section = models.CharField(max_length=2, null=True, blank=True)
    dob = models.DateField(max_length=8, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    # fatherName= models.CharField(max_length=100, null=True, blank=True)
    # motherName = models.CharField(max_length=100, null=True, blank=True)
    # current_address = models.CharField(max_length=200, null=True, blank=True)
    # parmanent_address = models.CharField(max_length=200, null=True, blank=True)
    # religion = models.CharField(max_length=20, null=True, blank=True)
    # phoneNumber = models.CharField(max_length=13, null=True, blank=True)
    # nationality = models.CharField(max_length=40, null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # updated_at = models.DateField(null=True, blank=True)
    # profile_pic = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100,null=True, blank=True)
    # blood_group = models.CharField(max_length=5, null=True, blank=True)
    # classRoom = models.IntegerField(null=True, blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Students"
    def __str__(self):
        return self.customuser.username
    