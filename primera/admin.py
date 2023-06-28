from django.contrib import admin
from .models import Author, Book
# Register your models here.

admin.site.site_header = 'Curso Django 0031'
admin.site.index_title = 'Panel de control '
admin.site.site_title = 'Administrador Django '



class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','title')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('created','name')

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book, BookAdmin)