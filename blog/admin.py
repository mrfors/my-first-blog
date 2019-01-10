from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class SutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('author', 'created_date', 'published_date') # список для фильтра
    search_fields = ('title', 'text') # список для поиска
    summer_not_fields = ('text',) # подключать поля для которых необходимо редактирования в админке с панелью

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date') # поля для оображения в админке
    list_filter = ('author', 'created_date', 'published_date') # список для фильтра
    search_fields = ('title', 'text') # список для поиска



#   admin.site.register(Post, PostAdmin)
admin.site.register(Post, SutAdmin)
