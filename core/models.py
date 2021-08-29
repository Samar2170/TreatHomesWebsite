from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

myList=['Air-Conditioned','TV-DTH', 'Study-Table','Heated-water','Toiletries','Meals','Parking','Kithcen','Housekeeping']

class Sites(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=400)
    pincode=models.CharField(max_length=6)

    city=models.CharField(max_length=200, null=True, blank=True)
    available=models.CharField(max_length=50, null=True, blank=True)

    image1=models.ImageField(upload_to='media/sites', null=True)

    image2=models.ImageField(upload_to='media/sites', null=True, blank=True)
    image3=models.ImageField(upload_to='media/sites', null=True, blank=True)
    image4=models.ImageField(upload_to='media/sites', null=True, blank=True)
    image5=models.ImageField(upload_to='media/sites', null=True, blank=True)
    image6=models.ImageField(upload_to='media/sites', null=True, blank=True)
    image7=models.ImageField(upload_to='media/sites', null=True, blank=True)

    n_reviews=models.PositiveIntegerField(null=True, blank=True)
    n_customers=models.PositiveIntegerField(null=True, blank=True)
    n_projects=models.PositiveIntegerField(null=True, blank=True)

    tagline=models.TextField(null=True, blank=True)

    n_services=ArrayField(models.CharField(max_length=200, null=True), size=15, default=myList)
    #
    n_type=models.CharField(max_length=200,null=True, blank=True)

    n_hours_stayed=models.PositiveIntegerField(null=True, blank=True)
    n_approved=models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.name
        

class FrontImages(models.Model):
    site_name=models.CharField(max_length=200)
    site_image=models.ImageField(upload_to='media/front_images', null=True)
    
    def __str__(self):
        return self.site_name

class Services(models.Model):
    name=models.CharField(max_length=300)
    head_image=models.ImageField(upload_to='media/service',null=True, blank=True)
    tag=models.TextField(null=True, blank=True)
    sites=models.PositiveIntegerField(null=True,blank=True)

    para=models.TextField(null=True)
    image1=models.ImageField(upload_to='media/services', null=True)

    image2=models.ImageField(upload_to='media/services', null=True, blank=True)
    image3=models.ImageField(upload_to='media/services', null=True, blank=True)
    image4=models.ImageField(upload_to='media/services', null=True, blank=True)

    def __str__(self):
        return self.name

class ServiceFeatures(models.Model):
    heading=models.CharField(max_length=200)
    brief=models.TextField()
    service=models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading

               
class Reviews(models.Model):
    name=models.CharField(max_length=200)
    sub_head=models.CharField(max_length=250)
    review=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='media/reviews',null=True, blank=True)

    def __str__(self):
        return self.name


class AncilServices(models.Model):
    name=models.CharField(max_length=200)
    brief=models.TextField()
    image=models.ImageField(upload_to='media/ancilServices', null=True, blank=True)

    def __str__(self):
        return self.name

class USP(models.Model):
    name=models.CharField(max_length=200)
    brief=models.TextField()

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question=models.TextField()
    answer=models.TextField()
    def __str__(self):
        return self.question


class Lead(models.Model):
    name=models.CharField(max_length=200, null=True)
    co_name=models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True)
    phone=models.CharField(max_length=13)
    n_guests=models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.name}, {self.co_name} -- Contact -- {self.phone}")

class PhoneLead(models.Model):
    phone=models.CharField(max_length=13)

 