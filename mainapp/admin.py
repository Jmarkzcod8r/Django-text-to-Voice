from django.contrib import admin
# from .models import Product, Section
from .models import *  # Product, Section, Post

# Register your models here.
admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Post)
# admin.site.register(BookInstance)