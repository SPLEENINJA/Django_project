from django.contrib import admin
from .models import BlogPost,Authors,Comment

admin.site.register(BlogPost)
admin.site.register(Authors)
admin.site.register(Comment)
