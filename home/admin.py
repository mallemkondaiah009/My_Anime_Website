from django.contrib import admin
from .models import Ghibli_Movies

class GhibliMoviesAdmin(admin.ModelAdmin):
    list_display=['title','image','link']

admin.site.register(Ghibli_Movies,GhibliMoviesAdmin)