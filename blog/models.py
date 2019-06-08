from django.db import models

# Create blog models here.
    #title
    #pubdate
    #body
    #image

class Blog(models.Model):
    title    = models.CharField(max_length=140)
    pub_date = models.DateTimeField()
    body     = models.TextField()
    image    = models.ImageField(upload_to='images/')

# Migrate

# Add to admin