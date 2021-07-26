from django.contrib import admin
from .models import Bid, Category, Photo, Comment, Listing

# Register your models here.
admin.site.register(Bid)
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Listing)
