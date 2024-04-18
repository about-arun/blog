from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
