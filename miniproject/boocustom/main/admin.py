from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'nickname',
        'country', 
        'image', 
        'greetings', 

        )
    search_fields = ('nickname',)



admin.site.register(Post, PostAdmin)


