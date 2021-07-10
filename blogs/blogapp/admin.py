
from django.contrib import admin

# Register your models here.
from .models import Blogpost,Contact



admin.site.register(Contact)

@admin.register(Blogpost)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyinject.js',)