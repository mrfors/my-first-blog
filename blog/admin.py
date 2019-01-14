from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .models import Pogar, Sevsk, Calendar


class SutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('author', 'created_date', 'published_date') # список для фильтра
    search_fields = ('title', 'text') # список для поиска
    summer_not_fields = ('text',) # подключать поля для которых необходимо редактирования в админке с панелью

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date') # поля для оображения в админке
    list_filter = ('author', 'created_date', 'published_date') # список для фильтра
    search_fields = ('title', 'text') # список для поиска
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date') # поля для оображения в админке
    list_filter = ('author', 'published_date') # список для фильтра
    search_fields = ('title', 'text') # список для поиска


#   admin.site.register(Post, PostAdmin)
admin.site.register(Post, SutAdmin)
admin.site.register(Pogar, SutAdmin)
admin.site.register(Sevsk, SutAdmin)
admin.site.register(Calendar, CalendarAdmin)
