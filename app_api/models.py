from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 180)
    post = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.post