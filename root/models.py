from django.db import models



class FrequentlyQuestions(models.Model):
    question = models.CharField(max_length=220)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering =['-created_at']


    def __str__(self):
        return self.question
# Create your models here.




class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name