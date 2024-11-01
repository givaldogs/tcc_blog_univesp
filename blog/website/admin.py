from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title',
                    'full_name', 'categories',
                     'deleted']
    search_fields = ['title', 'sub_title']
   # fields =('title', 'sub_title')

    def get_queryset(self, request) -> QuerySet:
        return Post.objects.filter(deleted=False)

admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
