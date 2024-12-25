from django.db import models

class Ghibli_Movies(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    link=models.URLField(max_length=200)

    def __str__(self):
        return self.title
