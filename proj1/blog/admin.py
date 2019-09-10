from django.contrib import admin
from .models import Post
from .models import Post_M,Comment

admin.site.register(Post)
admin.site.register(Post_M)
admin.site.register(Comment)
# Register your models here.
