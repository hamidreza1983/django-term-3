from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Profile
User = get_user_model()




class SpecialService(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering =['-created_at']


    def __str__(self):
        return self.title
    
class Skills(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    image = models.ImageField(upload_to='services', default='default.jpg')
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    status = models.BooleanField(default=False)
    facebook = models.CharField(max_length=220, default="#")
    twitter = models.CharField(max_length=220, default="#")
    instagram = models.CharField(max_length=220, default="#")
    linkdin = models.CharField(max_length=220, default="#")



    def __str__(self):
        return self.profile.email
    

    def truncate_char(self):
        return str(self.description)[:10]

class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Options(models.Model):
    title = models.CharField(max_length=300)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Services(models.Model):
    image = models.ImageField(upload_to='services', default='image.jpg')
    name = models.CharField(max_length=300)
    content = models.TextField()
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    generals = models.ManyToManyField(Options)
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    counted_view = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

class Comments(models.Model):
    product_name = models.CharField(max_length=100)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
