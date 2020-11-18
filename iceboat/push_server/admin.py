from django.contrib import admin
from .models import ImageData

class ImageDataAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'image']
admin.site.register(ImageData, ImageDataAdmin)