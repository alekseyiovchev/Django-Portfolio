from django.contrib import admin
from .models import *


class StackAdmin(admin.ModelAdmin):
    list_display = ('id','title','wiki','time_create','photo','done')
    list_display_links = ('id','title','wiki')
    search_fields = ('title','content')
    list_editable = ('done','photo')
    list_filter = ('done','time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Stack, StackAdmin)
admin.site.register(Category, CategoryAdmin)