from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to = 'images/') # how to put an image in. The upload to will save it in the media directory but then we specified images
    summary = models.TextField()
	
    def snippet(self):
        return self.summary[:100]	


class Job_Post(models.Model):
    title = models.CharField(max_length=140)
    pub_date = models.DateTimeField(blank = True, null=True) 
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title	
	
	
	
 
