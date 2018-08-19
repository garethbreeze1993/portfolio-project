from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to = 'images/') # how to put an image in. The upload to will save it in the media directory but then we specified images
    summary = models.CharField(max_length=200)


class Job_Post(models.Model):
    title = models.CharField(max_length=140)
    pub_date = models.DateTimeField() 
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title	
	
	
	
 
