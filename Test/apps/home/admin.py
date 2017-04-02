from django.contrib import admin
from apps.home.models import Home

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    model = Home
    list_display = ['nome', 'slug', 'texto']
    list_filter = ['slug']
    list_search = ['nome', 'slug']
    search_fields = ['nome', 'slug']

admin.site.register(Home, HomeAdmin)