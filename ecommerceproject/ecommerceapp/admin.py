from django.contrib import admin

# Register your models here.
from ecommerceapp.models import Category, Product


class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':['name']}
admin.site.register(Category,Categoryadmin)



class Productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    prepopulated_fields = {'slug':['name']}
    list_editable = ['price','stock','available']
    list_per_page = 20
admin.site.register(Product,Productadmin)