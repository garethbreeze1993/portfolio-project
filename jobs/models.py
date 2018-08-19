from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to = 'images/') # how to put an image in. The upload to will save it in the media directory but then we specified images
    summary = models.CharField(max_length=200)	
	
	
 
