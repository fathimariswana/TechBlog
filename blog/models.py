from ckeditor_uploader.fields import RichTextUploadingField
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
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    name = models.CharField(max_length=100)
    bloparent = models.ForeignKey(Blog, on_delete=models.CASCADE)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Reply(models.Model):
    name = models.CharField(default='Author')
    commentParent = models.ForeignKey(Comments, on_delete=models.CASCADE)
    replymsg = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name