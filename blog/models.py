from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_desc = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnail')
    content = models.TextField()

    def __str__(self):
        return self.title
