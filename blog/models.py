from django.db import models


class Blog_Post(models.Model):
    title = models.CharField(max_length=140)
    pub_date = models.DateTimeField() 
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title
		
    def summary(self):
        return self.body[:100] # returns first 100 characters of the body text, by using list splicing.	

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')	# returns date as Month day year.
# Create your models here.
