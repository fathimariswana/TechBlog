from django.contrib import admin
from .models import Category, Blog, Comments, Reply

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comments)
admin.site.register(Reply)

