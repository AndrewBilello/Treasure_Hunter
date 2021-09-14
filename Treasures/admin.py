from django.contrib import admin

from .models import Treasure, Post, Comment, Hint

admin.site.register(Treasure)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Hint)
