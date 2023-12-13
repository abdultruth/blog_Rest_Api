from django.contrib import admin


from .models import Comment, Feed
# Register your models here.
admin.site.register(Comment)
admin.site.register(Feed)