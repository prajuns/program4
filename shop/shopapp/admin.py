from django.contrib import admin
from . models import category,product

# Register your models here.

class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable =  ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(product,productadmin)