from django.db import models

class Blog_Post(models.Model):
    title = models.CharField(max_length=140)
    pub_date = models.DateTimeField() 
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

# Create your models here.
