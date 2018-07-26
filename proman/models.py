from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver

class department(models.Model):
    dep_name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.dep_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', default = 'iitg.png')
    title = models.CharField(max_length=10, blank=True)
    fname = models.CharField(max_length=200, blank=True)
    mname = models.CharField(max_length=200, blank=True)
    lname = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    dep = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
    desig = models.CharField(max_length=200, blank=True)
    descrip = models.TextField(blank=True)
    office = models.CharField(max_length=50, blank=True)
    phn_no = models.CharField(max_length=200,default='+91-361-258XXXX')
    resid = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.fname + " " + self.mname + " " + self.lname

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        profile.save()

class edu(models.Model):
    college = models.CharField(max_length=200, blank=True, default="")
    degree = models.CharField(max_length=50,blank=True, default="")
    descrip = models.CharField(max_length=200,blank=True, default="")
    startTime = models.CharField(max_length=50,blank=True, default="")
    endTime = models.CharField(max_length=50,blank=True, default="")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # ordering = ['-order_date']
    # class Meta:
    #     ordering = ['-created_at']

    def __str__(self):
        return self.degree + " " + self.descrip

class resInt(models.Model):
    descrip = models.CharField(max_length=200)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descrip

class workExp(models.Model):
    desig = models.CharField(max_length=200,blank=True, default="")
    firm = models.CharField(max_length=200,blank=True, default="")
    descrip = models.CharField(max_length=200,blank=True, default="")
    startTime = models.CharField(max_length=50,blank=True, default="")
    endTime = models.CharField(max_length=50,blank=True, default="")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.desig + " " + self.descrip

class course(models.Model):
    startYear = models.IntegerField(default=2017)
    endYear = models.IntegerField(default=2018)
    semester = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    course_code = models.CharField(max_length=6, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['-endYear']

    def __str__(self):
        return self.course_code + " " + self.name

class Project(models.Model):
    title = models.CharField(max_length=200, blank=True)
    PI = models.CharField(max_length=200, blank=True)
    FundingAgency = models.CharField(max_length=200, blank=True)
    syear = models.IntegerField(blank=True, default=2017)
    fyear = models.IntegerField(blank=True, default=2018)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['-fyear']
    def __str__(self):
        return self.title

class Publication(models.Model):
    descrip = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.descrip

class Book(models.Model):
    descrip = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.descrip

class Deg(models.Model):
    degree = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.degree

class ContinuingStudent(models.Model):
    name = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    degree = models.ForeignKey(Deg, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class CompletedStudent(models.Model):
    supervisor = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    thesisTitle = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    degree = models.ForeignKey(Deg, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class award(models.Model):
    descrip = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.descrip