from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','status','publish',)
    list_filter = ('status',)
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    list_editable = ('status',)

admin.site.register(Book)